import random
import numpy as np

from brainrender import Scene
from brainrender.actors import Points


def get_n_random_points_in_region(region, N):
    """
    Gets N random points inside (or on the surface) of a mes
    """

    region_bounds = region.bounds()
    X = np.random.randint(region_bounds[0], region_bounds[1], size=10000)
    Y = np.random.randint(region_bounds[2], region_bounds[3], size=10000)
    Z = np.random.randint(region_bounds[4], region_bounds[5], size=10000)
    pts = [[x, y, z] for x, y, z in zip(X, Y, Z)]

    ipts = region.insidePoints(pts).points()
    return np.vstack(random.choices(ipts, k=N))


scene = Scene(title="Labelled cells")

# Get a numpy array with (fake) coordinates of some labelled cells
mos = scene.add_brain_region("MOs", alpha=0.15)
coordinates = get_n_random_points_in_region(mos, 2000)

# Add to scene
scene.add(Points(coordinates, name="CELLS", colors="steelblue"))

# render
scene.content
scene.render()