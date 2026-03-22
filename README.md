# 🎬 AI Video Generation Pipeline

This project is a custom-built AI pipeline that converts a simple user idea into a short video with visuals, captions, and background music.

## 🚀 Features

* 🔹 Takes a user topic as input
* 🔹 Generates structured prompts (story-based)
* 🔹 Uses AI-generated or manual images (Leonardo)
* 🔹 Adds captions to each scene
* 🔹 Combines images into a video with transitions and music

---

## 🧠 How it works

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

## 📌 Example

Input:

```
AI in healthcare
```

Output:

* Scene 1: Problem in healthcare
* Scene 2: Introduction of AI
* Scene 3: AI helping humans
* Scene 4: Improved life
* Scene 5: Future vision

---

## 🛠 Tech Stack

* Python
* MoviePy
* Pillow (PIL)
* Requests (API-ready)

---

## ⚙️ Setup

```bash
git clone https://github.com/YOUR_USERNAME/ai-video-generation-pipeline.git
cd ai-video-generation-pipeline
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

Then enter:

* Topic (e.g. "AI in healthcare")
* Mode: manual / api

---

## 📈 Future Improvements

* 🔸 Full API-based image generation
* 🔸 Voiceover (text-to-speech)
* 🔸 Better scene transitions
* 🔸 Web interface

---

## 💡 Motivation

This project started as an experiment with no-code tools (n8n). It helped me quickly prototype the idea, but I realized I wanted more control and flexibility.

So I rebuilt the entire pipeline from scratch in Python, making it modular and extensible.

---

## 📬 Feedback

Open to suggestions and improvements!
