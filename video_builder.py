from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
import os
import textwrap


def add_caption_to_image(image_path, text, index):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 50)

    # Wrap text into multiple lines
    wrapped_text = textwrap.fill(text, width=30)

    draw.text(
        (50, img.height - 250),
        wrapped_text,
        font=font,
        fill="white",
        stroke_width=2,
        stroke_fill="black"
    )

    new_path = f"outputs/captioned_{index}.png"
    img.save(new_path)

    return new_path


def build_video(image_paths, captions):
    if not image_paths:
        print("❌ No images provided.")
        return

    clips = []
    new_paths = []

    # Add captions to images
    for i, path in enumerate(image_paths):
        captioned_path = add_caption_to_image(path, captions[i], i)
        new_paths.append(captioned_path)

    # Create video clips
    for path in new_paths:
        clip = (
            ImageClip(path)
            .set_duration(4)
            .resize(width=1280)
            .fadein(0.7)
            .fadeout(0.7)
        )
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    # Add music
    audio_path = "assets/music.mp3"
    if os.path.exists(audio_path):
        audio = AudioFileClip(audio_path)
        audio = audio.set_duration(video.duration)
        video = video.set_audio(audio)

    video.write_videofile("outputs/final_video.mp4", fps=24)