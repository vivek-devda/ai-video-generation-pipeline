# 🎬 AI Video Generation Pipeline

## Focus
This project demonstrates modular pipeline design for AI systems, including structured processing, fallback handling, and extensibility toward API-based automation workflows.

While currently focused on media generation, the architecture reflects patterns used in backend automation pipelines.

---

## 🎥 Demo

![Demo](assets/demo.gif)

**Example Input:**
"AI in healthcare"

## Flask API (Backend Simulation)

This project includes a Flask API layer to simulate how the pipeline can be deployed as a backend service.

Endpoint:
POST /generate

Example:
{
  "topic": "AI in healthcare"
}

Returns:
{
  "status": "success",
  "output": "outputs/final_video.mp4"
}

**Output:**
A short multi-scene video with captions, transitions, and music.

---

## ⚡ What This Does

**Input:**
"AI in healthcare"

**Output:**

* Structured story-based script
* Scene-wise captions
* Visual sequence (manual / API-ready)
* Final compiled video (MP4)

---

## 🧩 Pipeline Overview

```
User Input (Topic)
        ↓
Prompt Generator (structured narrative)
        ↓
Image Source (manual / API-ready)
        ↓
Caption Overlay (PIL)
        ↓
Video Builder (MoviePy)
        ↓
Final Video Output
```

---

## 📊 Results

* Generated 20+ test videos
* Avg generation time: ~15–30 seconds
* Supports multi-scene narrative structure
* Handles missing images with fallback logic

---

## ⚙️ Robustness

- Handles missing images using fallback assets
- Prevents full pipeline failure due to partial errors
- Ensures video generation completes even with incomplete inputs
- Designed for stable execution across multiple test runs

---

## 📂 Sample Output

* 🎬 Format: MP4
* ⏱ Duration: ~30–60 seconds
* 🎞 Scenes: 4–6
* 📁 Output: `outputs/final_video.mp4`

---

## 🚀 Features

* Converts a simple idea into a structured video pipeline
* Modular architecture (easy to extend)
* Caption overlay for each scene
* Video creation with transitions and background music
* Designed for automation workflows

---

## 🛠 Tech Stack

* Python
* MoviePy (video processing)
* Pillow / PIL (image + captions)
* Requests (API-ready integration)

---

## 📂 Project Structure

```
project/
├── main.py
├── app.py
├── pipeline/
│   ├── prompt.py
│   ├── image.py
│   ├── caption.py
│   └── video.py
├── assets/
├── outputs/
```

---

## ⚙️ Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/ai-video-generation-pipeline.git
cd ai-video-generation-pipeline
pip install -r requirements.txt
python main.py
```

Then enter:

* Topic: "AI in healthcare"
* Mode: manual / api

---

## 🎯 Why This Project?

Modern AI applications are not just models — they are pipelines that combine multiple components like prompting, media generation, and orchestration.

This project simulates real-world AI content systems used in:

* marketing automation
* content generation
* AI media tools

---

## 💼 Use Cases

- AI-generated educational videos
- Social media content automation
- Marketing and promotional video generation
- Rapid prototyping for AI media tools

---

## 🧠 System Design Highlights

* Modular pipeline architecture
* Separation of concerns (prompt → image → video)
* Extensible for API integrations (image generation, TTS)
* Designed for both manual and automated workflows

---

## 🧠 Design Decisions

- Built as a modular pipeline instead of a monolithic script to improve scalability and maintainability
- Separated prompt generation from rendering to allow flexible content control
- Designed image layer to support both manual assets and future API integrations
- Used step-wise processing to make debugging and iteration easier
- Prioritized reliability by allowing partial pipeline execution even with missing inputs

---

## ⚠️ Important Note

Currently, images are manually sourced for demonstration purposes.

The pipeline is designed to support full API-based image generation, making it easily extendable into a fully automated system.

---

## 📈 Future Improvements

* Full API-based image generation
* Text-to-speech (voiceover)
* Improved transitions and animations
* CLI support (`--topic`, `--mode`)
* Web interface for non-technical users

---

## 🔌 Extensibility

The system is designed to easily integrate:

- Text-to-Image models (Stable Diffusion, APIs)
- Text-to-Speech (voice narration)
- Frontend interfaces (web apps)
- Scheduling and automation workflows

---

## 💡 Motivation

This project was initially prototyped using no-code tools (n8n), then rebuilt from scratch in Python to gain deeper control over system design and automation workflows.

---

## 📬 Feedback

Open to suggestions, improvements, and collaboration!

---

## 👨‍💻 Author

Vivek Devda
B.Tech Artificial Intelligence & Machine Learning

GitHub: https://github.com/vivek-devda
