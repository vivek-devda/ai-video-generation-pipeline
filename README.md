# 🎬 AI Video Generation Pipeline

An AI-powered pipeline that transforms a simple text prompt into a structured multi-scene video with captions, visuals, and background music.

This project demonstrates how real-world AI systems are built using modular pipelines, media processing, and automation workflows.

---

## 🎥 Demo

![Demo](assets/demo.gif)

**Example Input:**
"AI in healthcare"

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

## 🧠 System Design Highlights

* Modular pipeline architecture
* Separation of concerns (prompt → image → video)
* Extensible for API integrations (image generation, TTS)
* Designed for both manual and automated workflows

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
