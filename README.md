# 🎬 AI Video Generation Pipeline

An end-to-end AI-powered pipeline that transforms a simple text prompt into a structured multi-scene video with captions, visuals, and background music.

This project demonstrates how real-world AI content systems are built using modular pipelines and media processing.

---

## 🎥 Demo

![Demo](assets/demo.gif)

> Example input: **"AI in healthcare"**
> Output: A short video with multiple scenes, captions, and transitions.

---

## ⚡ What This Does

Input:

```
"AI in healthcare"
```

Output:

* Structured story-based script
* Scene-wise visual generation (manual/API-ready)
* Caption overlay on each scene
* Final compiled video (MP4 format)

---

## 🧩 Pipeline Overview

User Input
↓
Prompt Generator (structured narrative)
↓
Image Generation (manual / API-ready)
↓
Caption Overlay (PIL)
↓
Video Builder (MoviePy)
↓
Final Video Output

---

## 📂 Sample Output

* 🎬 Format: MP4
* ⏱ Duration: ~30–60 seconds
* 🎞 Scenes: 4–6
* 📁 Output Location: `outputs/final_video.mp4`

---

## 🚀 Features

* Converts a simple idea into a full video pipeline
* Modular architecture (easy to extend)
* Supports manual and API-based image generation
* Automatic caption overlay for each scene
* Video creation with transitions and background music

---

## 🛠 Tech Stack

* **Python**
* **MoviePy** – video processing
* **Pillow (PIL)** – image & caption rendering
* **Requests** – API integration (ready for extensions)

---

## ⚙️ Quick Start

```bash
git clone https://github.com/vivek-devda/ai-video-generation-pipeline.git
cd ai-video-generation-pipeline
pip install -r requirements.txt
python main.py
```

Then enter:

```
Topic: AI in healthcare
Mode: manual / api
```

---

## 🎯 Why This Project?

Modern AI applications are not just models — they are **pipelines** that combine multiple components like prompting, media generation, and orchestration.

This project focuses on building such a system from scratch, simulating real-world AI content generation workflows used in:

* Marketing automation
* YouTube content generation
* AI media tools

---

## 🧠 System Design Highlights

* Modular pipeline architecture
* Separation of concerns (prompt → image → video)
* Extensible for API integrations (image generation, TTS)
* Supports both manual and automated workflows

---

## ⚠️ Challenges & Learnings

* Debugging media processing and library compatibility issues
* Designing a clean pipeline flow across multiple components
* Managing transitions between text, images, and video
* Understanding real-world AI system design beyond simple scripts

---

## 📈 Future Improvements

* Full API-based image generation
* Text-to-speech voiceover integration
* Improved transitions and animations
* CLI-based input support (`--topic`, `--mode`)
* Web interface for non-technical users

---

## 💡 Motivation

This project was initially prototyped using no-code tools (n8n).
It was later rebuilt entirely in Python to gain deeper control, flexibility, and a better understanding of backend AI systems.

---

## 📬 Feedback

Open to suggestions, improvements, and collaboration!

---

## 👨‍💻 Author

**Vivek Devda**
B.Tech Artificial Intelligence & Machine Learning

GitHub: https://github.com/vivek-devda
