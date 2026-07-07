# 🩺 Real Doctor AI Agent
### Vision + Voice Multimodal Medical Assistant powered by Llama 3.2 Vision, Whisper & ElevenLabs

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Groq](https://img.shields.io/badge/Groq-Llama%203.2%20Vision-orange)
![Whisper](https://img.shields.io/badge/Whisper-STT-green)
![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-purple)
![Gradio](https://img.shields.io/badge/Gradio-WebUI-red)
![License](https://img.shields.io/badge/License-MIT-success)

</p>

---

# 🏥 Overview

Real Doctor AI Agent is a multimodal healthcare assistant capable of understanding both **patient speech** and **medical images**.

The system allows a patient to speak naturally while uploading an image of the affected body part. The AI combines both modalities using a Vision Language Model and produces a concise medical opinion before responding back using realistic synthesized speech.

Instead of functioning as a simple chatbot, the application mimics the workflow of a virtual doctor consultation.

---

# 🚀 Features

- 🎤 Speech-to-Text using Groq Whisper
- 👁️ Vision-based Medical Image Understanding
- 🤖 Llama 3.2 Vision for Medical Reasoning
- 🔊 Natural Voice Responses using ElevenLabs
- 🖼️ Image Analysis
- 💬 Conversational AI Experience
- 🌐 Gradio Interface
- ⚡ End-to-End Multimodal Pipeline
- 🧠 Prompt Engineered Medical Responses

---

# 🎯 Problem Statement

Patients often struggle to obtain quick preliminary guidance for common medical concerns.

This project demonstrates how multimodal AI can assist patients by combining:

- Spoken symptoms
- Medical images
- Large Vision Language Models
- Natural voice interaction

to simulate an intelligent virtual doctor.

---

# 🏗 System Architecture

```

Patient
│
├── Voice Input
│
├── Medical Image
│
▼

Groq Whisper (Speech Recognition)
│
▼

Patient Query

│
├──────────────┐
│ │
▼ ▼

Medical Image Prompt

│ │

└──────┬───────┘
▼

Llama 3.2 Vision

▼

Medical Diagnosis

▼

ElevenLabs

▼

Voice Response

```

---

# 🧠 AI Pipeline

## Step 1 — Patient Speaks

The patient records their symptoms through the microphone.

Example:

> "I have red spots on my face and itching for the last two days."

---

## Step 2 — Speech Recognition

The recorded audio is processed using

**Groq Whisper Large v3**

Output:

```

"I have red spots on my face..."

```

---

## Step 3 — Image Understanding

The uploaded image is converted into Base64 and passed to

**Llama 3.2 Vision**

along with

- doctor's system prompt
- patient's symptoms

This enables multimodal reasoning.

---

## Step 4 — Medical Reasoning

The LLM performs

- symptom understanding
- visual inspection
- differential reasoning
- possible remedies

while remaining concise.

---

## Step 5 — Voice Generation

The generated diagnosis is converted into natural speech using

**ElevenLabs TTS**

The user hears the doctor's response instantly.

---

# 🛠 Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| UI | Gradio |
| Speech Recognition | Groq Whisper Large v3 |
| Vision Model | Llama 3.2 90B Vision |
| Voice Generation | ElevenLabs |
| Image Processing | Base64 Encoding |
| AI Provider | Groq |
| Prompt Engineering | Custom Medical Prompt |

---

# 📂 Project Structure

```

voicebot/

│

├── gradio_app.py
│ Main Application

├── brain_of_the_doctor.py
│ Vision AI

├── voice_of_the_patient.py
│ Whisper STT

├── voice_of_the_doctor.py
│ ElevenLabs TTS

├── acne.jpg
│ Sample Medical Image

├── .env
│ API Keys

└── README.md

```

---

# 🔥 Core Components

## 🎤 Speech Recognition

Uses

**Groq Whisper Large v3**

to convert patient speech into text.

Advantages

- Fast
- Accurate
- Low latency

---

## 👁 Vision Understanding

The uploaded image is encoded into Base64 and passed directly to

Llama 3.2 Vision.

The model simultaneously understands

- image
- patient symptoms

to produce context-aware responses.

---

## 🧠 Medical Reasoning

A carefully engineered system prompt instructs the model to

- behave like a doctor
- avoid mentioning AI
- provide concise responses
- suggest remedies
- avoid markdown formatting

---

## 🔊 Voice Synthesis

The doctor's response is synthesized using

ElevenLabs

providing a natural conversational experience.

---

# 📸 Example Workflow

Input

Voice

> "I have acne on my forehead."

Image

Patient uploads acne image.

↓

Whisper

↓

Patient Transcript

↓

Llama Vision

↓

Diagnosis

↓

ElevenLabs

↓

Doctor Voice Response

---

# ⚙ Installation

Clone repository

```bash
git clone https://github.com/udayvimal/LLM-PORTFOLIO-UDAY.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create

```
.env
```

```
GROQ_API_KEY=your_key

ELEVENLABS_API_KEY=your_key
```

Run

```bash
python gradio_app.py
```

---

# 💡 Future Improvements

- Medical RAG using clinical documents
- Conversation memory
- Patient history
- Follow-up questioning
- Multi-language support
- Appointment booking
- Prescription generation
- Medical report PDF
- Disease confidence score
- Doctor recommendation engine

---

# ⚠ Disclaimer

This project is intended solely for educational and research purposes.

It does **not** replace consultation with licensed healthcare professionals.

---

# 👨‍💻 Author

**Uday Vimal**

AI Engineer

- Python
- LLMs
- RAG
- FastAPI
- LangGraph
- Vision AI
- Agentic AI
- Multimodal Systems

GitHub

https://github.com/udayvimal
