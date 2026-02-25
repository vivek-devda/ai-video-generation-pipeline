# AI Video Generation Automation Pipeline

A fully automated end-to-end AI video generation pipeline built using n8n, Python, Flask, and AI APIs. This system demonstrates workflow automation, webhook-based backend integration, and automated media processing without manual intervention.

---

## Key Features

- Automated video idea generation using AI APIs
- Automatic image prompt creation and image generation
- Webhook-based communication between automation workflow and backend server
- Fully automated video generation using Python and MoviePy
- End-to-end pipeline orchestration using n8n workflow automation
- Modular and scalable pipeline architecture

---

## Tech Stack

**Programming & Backend**
- Python
- Flask
- REST API Integration
- Webhooks

**Automation & AI**
- n8n Workflow Automation
- OpenRouter AI API
- Prompt Engineering

**Media Processing**
- MoviePy
- Automated image-to-video conversion

**Tools & Platforms**
- GitHub
- ngrok
- JSON

---

## System Architecture

n8n Workflow
↓
AI API (Idea Generation)
↓
Image Generation API
↓
Webhook (Flask Server via ngrok)
↓
Python Automation Script
↓
Video Generation (MoviePy)
↓
Output Video File


---

## How It Works

1. n8n workflow triggers automation pipeline
2. AI generates video idea using API
3. System converts idea into image prompt
4. Image is generated automatically via image API
5. n8n sends image URL to Flask webhook server
6. Python script downloads image and generates video using MoviePy
7. Final video output is saved automatically

---

## Project Structure

generate_video.py # Video generation script
server.py # Flask webhook server
workflow.json # n8n automation workflow
requirements.txt # Project dependencies
README.md # Project documentation

---

## Engineering Concepts Demonstrated

- Workflow Automation
- Backend Development
- Webhook Integration
- API Integration
- Automation Pipeline Design
- Client–Server Architecture
- System Integration
- Media Processing Automation

---

## Installation & Usage

1. Install dependencies:
pip install -r requirements.txt

2. Run Flask server:
python server.py

4. Start ngrok:
ngrok http 5000

5. Import `workflow.json` into n8n and run workflow

---

## Author

Vivek Devda  
B.Tech Artificial Intelligence & Machine Learning  
GitHub: https://github.com/your-username
