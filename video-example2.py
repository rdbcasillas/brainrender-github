import brainrender
from brainrender import Scene
from brainrender.video import VideoMaker
import vedo

# Create a scene
scene = Scene("my video")
scene.add_brain_region("TH")

# Create an instance of video maker
vm = VideoMaker(scene, "examples", "vid1")

# make a video with the custom make frame function
# this just rotates the scene
vm.make_video(elevation=2, duration=2, fps=15)

vedo.show(*scene.renderables)