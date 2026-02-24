import requests
import os
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

# Create images folder
image_folder = "images"
os.makedirs(image_folder, exist_ok=True)

# Image URLs
image_urls = [
    "https://picsum.photos/1024/1024?random=1",
    "https://picsum.photos/1024/1024?random=2",
    "https://picsum.photos/1024/1024?random=3",
    "https://picsum.photos/1024/1024?random=4",
    "https://picsum.photos/1024/1024?random=5"
]

# Download images
image_paths = []

print("Downloading images...")

for i, url in enumerate(image_urls):
    path = os.path.join(image_folder, f"img{i}.jpg")
    response = requests.get(url)

    with open(path, "wb") as f:
        f.write(response.content)

    image_paths.append(path)
    print(f"Downloaded {path}")

# Create video
print("Creating video...")

# Each image shows for 2 seconds
durations = [2] * len(image_paths)

# Create smooth video clip
clip = ImageSequenceClip(image_paths, durations=durations)

# Set professional video settings
clip.write_videofile(
    "output.mp4",
    fps=24,                 # smooth video (24 FPS standard)
    codec="libx264",
    audio=False,
    preset="medium"
)