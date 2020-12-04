import brainrender

brainrender.SHADER_STYLE = 'cartoon'
from brainrender.scene import Scene
from brainrender.animation.video import BasicVideoMaker as VideoMaker




scene = Scene()
scene.add_brain_regions(['RN'], color="violet")


# Create an instance of VideoMaker with our scene
vm = VideoMaker(scene, niters=30)  # niters = number of frames

# Make a video!
#vm.make_video(
#    elevation=1, roll=5
#)  # specify how the scene rotates at each frame

scene.render()