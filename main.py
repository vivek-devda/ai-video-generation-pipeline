from prompt_generator import generate_prompts
from image_generator import generate_images
from video_builder import build_video


def main():
    topic = input("Enter topic: ")
    mode = input("Enter mode (manual/api): ")

    image_prompts, captions = generate_prompts(topic)

    if mode == "manual":
        images = [
            "outputs/image_0.jpg",
            "outputs/image_1.jpg",
            "outputs/image_2.jpg",
            "outputs/image_3.jpg",
            "outputs/image_4.jpg",
        ]
    else:
        images = generate_images(image_prompts)

    build_video(images, captions)

    print("✅ Video created successfully!")


if __name__ == "__main__":
    main()