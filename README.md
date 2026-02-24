# AI Video Generation Pipeline (Fully Automated)

This project is a fully automated end-to-end video generation pipeline built using n8n and Python.

It automatically performs:

• Idea generation using AI
• Image prompt generation
• Image generation using AI
• Video creation using Python automation
• Fully automated workflow with no manual intervention

---

## Technologies Used

• n8n (workflow automation)
• Python (video generation with MoviePy)
• OpenRouter AI (text generation)
• Pollinations AI / Picsum (image generation)
• Flask (local video generation server)

---

## Pipeline Architecture

Idea Generator → Image Prompt Generator → Image Generator → Python Video Generator → Final Video Output

---

## How it works

1. n8n generates a video idea
2. Converts idea into image prompt
3. Generates image automatically
4. Sends image to Python server
5. Python creates video automatically
6. Final video saved as output.mp4

---

## Demo Output

See output.mp4 file in this repository.

---

## Workflow File

Import workflow.json into n8n to run the automation.

---

## Fully Automated

No manual intervention required.

---

## Author

Vivek Devda
B.Tech Artificial Intelligence & Machine Learning
