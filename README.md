# Uday Vimal — AI Engineering Portfolio

Agentic AI · LLM Applications · Vision + Voice · Python ML · Data Analytics

---

## Key Results

- **Real Doctor AI Agent** — full multimodal pipeline: patient speaks, uploads an image, Llama 3.2 Vision diagnoses, ElevenLabs speaks back. End-to-end in a single Gradio session.
- **AI Business Reporting pipeline** — Groq Llama 3.3 70B writes a complete executive summary and Voice-of-Customer sentiment report from raw CSVs in under 30 seconds, replacing 2–4 hours of manual analyst work per cycle.
- **Influencer Campaign Tracker** — computed ROI, ROMI, CPA, and engagement across 40 influencers on 5 platforms; AI-ranked with SCALE / MONITOR / OPTIMIZE / DROP flags and strategic recommendations from Llama 3.3 70B.
- **Blood Test Agentic AI** — autonomous CrewAI agent reads a blood test PDF, compares values against reference ranges, and generates a plain-English medical summary without human intervention.

---

## About this repository

These projects were built individually during my B.Tech — across coursework, internships, and personal exploration — and bulk-migrated into this consolidated repo once I set up GitHub properly. Some folder names reflect the original working names I used at the time; I have left them as-is rather than silently rename things that already have links shared elsewhere. The two AI-analytics projects (`ai-business-reporting-sentiment` and `influencer-campaign-tracker`) are also available as standalone repos at their own URLs — both copies are kept in sync.

---

## Projects

| Folder | Description |
|---|---|
| [REAL_DOCTOR_AIAGENT](REAL_DOCTOR_AIAGENT/) | Multimodal medical agent: patient voice (Whisper STT) + image (Llama 3.2 Vision) → doctor-style voice response (ElevenLabs TTS) via Gradio |
| [FINANCE_AI_AGENT](FINANCE_AI_AGENT/) | Banking AI analyst with interactive dashboard: HuggingFace Transformers + RAG pipeline; predicts spending risk, EMI load, savings patterns |
| [Medical_AIAGENT](Medical_AIAGENT/) | Mini medical agent suite: symptom checker, medicine suggestion, diet assistant — built with Mistral and custom LLM integration |
| [BLOOD_TEST_AGENTIC_AI](BLOOD_TEST_AGENTIC_AI/) | Autonomous CrewAI agent: reads blood test PDFs, extracts values, compares with reference ranges, generates a plain-English medical summary |
| [Image_Recognition_Chatbot-master](Image_Recognition_Chatbot-master/) | Vision LLM for image classification and captioning using BLIP, CLIP, and Vision Transformers; designed as a plug-in vision module |
| [ai-business-reporting-sentiment](ai-business-reporting-sentiment/) | LLM pipeline: Groq Llama 3.3 70B writes executive summaries + VoC sentiment reports from raw CSVs in <30 seconds; includes n8n automation workflow — also at [standalone repo](https://github.com/udayvimal/ai-business-reporting-sentiment) |
| [influencer-campaign-tracker](influencer-campaign-tracker/) | 40-influencer campaign analytics across 5 platforms: ROI/ROMI/CPA/CTR computed, AI-ranked with SCALE/DROP flags and Groq-generated strategy report — also at [standalone repo](https://github.com/udayvimal/influencer-campaign-tracker) |
| [ADDITIONAL_PYTHON_WORK](ADDITIONAL_PYTHON_WORK/) | 6 Python ML projects: fake news detection, hotel booking prediction, movie recommendation, road sign detection, user authentication, YouTube view-count prediction |
| [JAVASCRIPT_WORK](JAVASCRIPT_WORK/) | Full-stack eCommerce frontend (HTML / CSS / JavaScript) demonstrating AI-agent + browser UI integration |

---

## Tech stack

| Area | Technologies |
|---|---|
| Agentic AI | CrewAI, multi-agent pipelines, tool calling |
| LLMs | Groq (Llama 3.3 70B), OpenAI, Gemini, Mistral, HuggingFace Transformers |
| Vision | Llama 3.2 Vision, BLIP, CLIP, ViT, CNN |
| Voice | ElevenLabs TTS, Groq Whisper STT |
| RAG | FAISS, ChromaDB, PDF/text embedding |
| Automation | n8n scheduled workflows |
| Python ML | scikit-learn, pandas, NumPy, matplotlib, seaborn, ETL pipelines |
| UI / Frontend | Gradio, FastAPI, Streamlit, JavaScript / HTML / CSS |

---

## Contact

**Email:** udayvimal08@gmail.com  
**GitHub:** [github.com/udayvimal](https://github.com/udayvimal)  
**LinkedIn:** [linkedin.com/in/uday-vimal-9a1a3a253](https://linkedin.com/in/uday-vimal-9a1a3a253)
