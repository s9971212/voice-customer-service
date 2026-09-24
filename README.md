# voice-customer-service

![LICENSE](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![PyCharm](https://img.shields.io/badge/PyCharm-blue)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-blue)  
![pydantic-settings](https://img.shields.io/badge/pydantic--settings-2.15.0-orange)
![uvicorn](https://img.shields.io/badge/uvicorn-0.53.0-orange)
![fastapi](https://img.shields.io/badge/fastapi-0.141.1-orange)
![python-multipart](https://img.shields.io/badge/python--multipart-0.0.32-orange)
![faster-whisper](https://img.shields.io/badge/faster--whisper-1.2.1-orange)
![librosa](https://img.shields.io/badge/librosa-1.0.0-orange)
![numpy](https://img.shields.io/badge/numpy-2.5.3-orange)
![openai](https://img.shields.io/badge/openai-3.19.0-orange)
![edge-tts](https://img.shields.io/badge/edge--tts-7.2.8-orange)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.53-orange)
![PyMySQL](https://img.shields.io/badge/PyMySQL-1.2.0-orange)  
![MySQL](https://img.shields.io/badge/MySQL-8.0.33-green)

English | [中文](./README_zh-TW.md)

## <br/> 📋 Table of Contents

- ✨ [Introduction](#introduction)
- ⚙️ [Tech Stack](#tech-stack)
- 🚀 [Quick Start](#quick-start)

## <br/> <a name="introduction">✨ Introduction</a>

A FastAPI-based voice customer service application that enables users to interact with an AI assistant through both text and voice. The system combines speech recognition, LLM-powered conversation, and text-to-speech to provide a complete voice-based customer service experience.

For data storage, MySQL is used as the Relational Database Management System (RDBMS). The high reliability and efficiency of MySQL ensures that large datasets can be managed and queried efficiently.

<br/>**Key Features**

- Send text messages to the AI assistant through a REST API.

- Upload audio recordings and convert speech into text using Faster Whisper.

- Convert the AI response back into speech using Edge TTS.

- Uses OpenAI-powered sessions to handle user conversations.

- Provides asynchronous REST APIs for text and voice interactions.

- Supports multipart file uploads for audio input.

## <br/> <a name="tech-stack">⚙️ Tech Stack</a>

- Python
- uvicorn [📄](https://uvicorn.dev/)
- fastapi [📄](https://fastapi.tiangolo.com/)
- faster-whisper
- openai [📄](https://openai.com/)
- edge-tts [📄](https://edge-tts.com/)
- SQLAlchemy [📄](https://www.sqlalchemy.org/=)
- MySQL [📄](https://www.mysql.com/)

## <br/> <a name="quick-start">🚀 Quick Start</a>

Follow these steps to set up the project locally on your machine.

<br/>**Prerequisites**

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/)
- [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows) | [Visual Studio Code](https://code.visualstudio.com/download?_exp_download=d53503e735)
- [MySQL](https://www.mysql.com/downloads/)
- [Git](https://git-scm.com/)

<br/>**Cloning Repository**

```bash
git clone {git remote url}
```

<br/>**Create virtual environment**

```bash
python -m venv .venv
```

<br/>**Install project dependencies**

```bash
pip install -e .
```

<br/>**Create .env file**

Here is how you can copy .env.example to create a new .env on your machine:

macOS / Linux
```bash
cp .env.example .env
```

Windows (Command Prompt / CMD)
```bash
copy .env.example .env
```

Windows (PowerShell)
```bash
Copy-Item .env.example .env
```

<br/>**Start application**

After installing everything and configuring .env, run:

```bash
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs to verify that all APIs are documented in Swagger. If they are, your environment is probably set up correctly.
