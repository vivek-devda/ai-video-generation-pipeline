from flask import Flask, request, jsonify
import requests
import os

from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

app = Flask(__name__)

@app.route("/generate-video", methods=["POST"])
def generate_video():

    try:

        # Get JSON from n8n
        data = request.json
        image_url = data.get("image_url")

        if not image_url:
            return jsonify({"error": "No image_url provided"}), 400

        print("\nDownloading images from base URL:", image_url)

        # Folder to store frames
        image_folder = "images"
        os.makedirs(image_folder, exist_ok=True)

        image_paths = []

        # Number of frames
        NUM_IMAGES = 20

        # Total video duration in seconds (you set 18)
        TOTAL_DURATION = 18

        duration_per_image = TOTAL_DURATION / NUM_IMAGES

        # Download DIFFERENT image each time using variation parameter
        for i in range(NUM_IMAGES):

            img_path = os.path.join(image_folder, f"frame{i}.jpg")

            unique_url = image_url + f"&variation={i}"

            print("Downloading:", unique_url)

            response = requests.get(unique_url)

            with open(img_path, "wb") as f:
                f.write(response.content)

            image_paths.append(img_path)

        print("All frames downloaded successfully")

        # Delete old video if exists
        if os.path.exists("output.mp4"):
            os.remove("output.mp4")

        print("Rendering video...")

        # Create video with equal duration per frame
        clip = ImageSequenceClip(
            image_paths,
            durations=[duration_per_image] * NUM_IMAGES
        )

        # Export video
        clip.write_videofile(
            "output.mp4",
            codec="libx264",
            audio=False,
            fps=24
        )

        print("\nVIDEO GENERATED SUCCESSFULLY")
        print("Total duration:", TOTAL_DURATION, "seconds")
        print("Frames:", NUM_IMAGES)
        print("Duration per frame:", duration_per_image, "seconds\n")

        return jsonify({
            "status": "success",
            "duration": TOTAL_DURATION,
            "frames": NUM_IMAGES
        })

    except Exception as e:

        print("ERROR:", str(e))

        return jsonify({
            "status": "error",
            "message": str(e)
        })


if __name__ == "__main__":
    app.run(port=5000)