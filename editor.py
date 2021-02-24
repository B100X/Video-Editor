# pip install moviepy

# Importing libraries.
from moviepy.editor import *


# Loading video DSA GFG intro video.
clip = VideoFileClip("dsa_geek.webm")


# Clipping of the video getting video for only starting 10 seconds.
clip = clip.subclip(0, 10)

# Rotating video by 180 degree.
clip = clip.rotate(180)

# Reduce the audio volume (volume x 0.5)
clip = clip.volumex(0.5)

# Showing clip
clip.ipython_display(width = 280)
