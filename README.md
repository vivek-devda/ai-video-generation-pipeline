# AI Automated Video Generation Pipeline

This project is a fully automated AI-powered video generation pipeline built using n8n, Python, and MoviePy.

## Features

• Fully automated workflow  
• AI-generated video ideas  
• AI-generated image prompts  
• Automated image generation  
• Automated video rendering  
• Cloud-to-local webhook integration  

## Architecture

n8n Cloud → Webhook → Python Flask Server → MoviePy → Video Output

## Technologies Used

- Python
- Flask
- MoviePy
- n8n
- AI Image Generation API

## How it Works

1. n8n generates video idea and prompt
2. AI generates image
3. n8n sends image URL to Python webhook
4. Python downloads images
5. MoviePy renders video automatically

## Output

Automated video generation without manual intervention.

## Author

Vivek Devda