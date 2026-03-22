def generate_prompts(topic):
    image_prompts = [
        f"{topic}: A human struggling with daily tasks, realistic scene",
        f"{topic}: A futuristic AI robot enters the home, cinematic lighting",
        f"{topic}: AI helping humans, cleaning, assisting elderly, ultra realistic",
        f"{topic}: Humans living easier and happier lives with AI",
        f"{topic}: Future world where humans and AI coexist peacefully"
    ]

    captions = [
        f"People face daily challenges related to {topic}",
        f"New AI technology begins to emerge",
        f"AI starts helping humans in real life",
        f"Life becomes easier with AI support",
        f"A future where humans and AI work together"
    ]

    return image_prompts, captions