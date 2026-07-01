# 🎬 AI Video Generation Pipeline

## 🎬 Overview

A multi-stage video generation pipeline that transforms a user-provided topic into a captioned MP4 video through template-based content generation, media processing, and automated rendering workflows.

The project demonstrates modular software design, media processing automation, and extensible pipeline architecture for future AI integrations.

---

## 🎥 Demo

![Demo](assets/demo.gif)

**Example Input:**
"AI in healthcare"

## Features

* Topic-based content generation
* Template-driven scene and caption creation
* Automatic caption overlay on images
* Multi-scene video compilation
* Fade-in and fade-out transitions
* Background music integration
* MP4 video export
* Modular and extensible architecture

---

## 🧩 Pipeline Workflow

```
User Topic
 ↓
Template-Based Prompt & Caption Generation
 ↓
Manual Image Selection
(Future: API-Based Images)
 ↓
Caption Rendering (Pillow)
 ↓
Video Composition (MoviePy)
 ↓
Final MP4 Output
```

---

# Example

Input:

AI in Healthcare

Generated Scenes:

1. Daily challenges related to AI in healthcare
2. Emerging AI technologies
3. AI assisting people in real-world scenarios
4. Improved quality of life through AI
5. Future collaboration between humans and AI

Output:

- Captioned images
- Background music
- Compiled MP4 video

---


## 🛠 Tech Stack

* Python
* MoviePy (video composition and rendering)
* Pillow (caption rendering and image processing)
* textwrap (dynamic text formatting)

---

## Engineering Highlights

* Designed a modular pipeline architecture with clearly separated responsibilities.
* Implemented reusable processing stages for prompt generation, media processing, and video rendering.
* Applied modular workflow design principles to transform a user-provided topic into a complete media output through multiple independent processing stages.
* Structured the project for future integration with image-generation APIs and text-to-speech systems.

---

## 📂 Project Structure

```
project/
├── main.py
├── prompt_generator.py
├── image_generator.py
├── video_builder.py
├── assets/
├── outputs/
```
---

## 📊 Results

* Supports multi-scene narrative structure
* Typical generation time: ~15–30 seconds on local execution

---

## 📂 Sample Output

* 🎬 Format: MP4
* ⏱ Duration: ~30–60 seconds
* 🎞 Scenes: 4–6
* 📁 Output: `outputs/final_video.mp4`

---

## 🎯 Why This Project?

Modern content systems are often built as pipelines that combine multiple processing stages such as content generation, media handling, and rendering workflows.

This project focuses on modular design and automation principles while providing extension points for future AI integrations.

This project simulates real-world AI content systems used in:

* marketing automation
* content generation
* AI media tools

---

## 💼 Use Cases

- Educational video generation prototypes
- Social media content automation
- Marketing and promotional video generation
- Rapid prototyping for AI media tools

---

## 🧠 Design Decisions

- Built as a modular pipeline instead of a monolithic script to improve scalability and maintainability
- Separated prompt generation from rendering to allow flexible content control
- Designed image layer to support both manual assets and future API integrations
- Used step-wise processing to make debugging and iteration easier
- Designed the workflow as independent processing stages to simplify debugging and future enhancements.

---

## ⚠️ Important Note

Currently, images are manually sourced for demonstration purposes.

The image layer was intentionally separated from the rendering pipeline to simplify future integration with image-generation APIs and automated media workflows.

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

## Key Learning Outcomes

- Modular software design
- Media processing pipelines
- Workflow orchestration
- Automation system development
- Extensible architecture design

---

## ⚙️ Quick Start

```bash
git clone https://github.com/vivek-devda/ai-video-generation-pipeline.git
cd ai-video-generation-pipeline
pip install -r requirements.txt
python main.py
```

Then enter:

- Topic: AI in healthcare
- Mode: manual

---


## 📬 Feedback

Open to suggestions, improvements, and collaboration!

---

## 👨‍💻 Author

Vivek Devda
B.Tech Artificial Intelligence & Machine Learning

GitHub: https://github.com/vivek-devda
