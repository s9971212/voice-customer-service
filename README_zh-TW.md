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

[English](./README.md) | 中文

## <br/> 📋 目錄

- ✨ [簡介](#introduction)
- ⚙️ [技術堆疊](#tech-stack)
- 🚀 [快速入門](#quick-start)

## <br/> <a name="introduction">✨ 簡介</a>

這是一個基於 FastAPI 開發的 AI 語音客服系統，支援使用者透過文字或語音與 AI 助理進行互動。系統整合了語音辨識（Speech-to-Text）、大型語言模型（LLM）以及文字轉語音（Text-to-Speech），提供完整的 AI 語音客服體驗。

在資料儲存方面，採用 MySQL 作為關聯式資料庫管理系統 (RDBMS)。MySQL 的高可靠性和高效率可確保有效管理和查詢大型資料集。

<br/>**主要功能**

- 透過 REST API 傳送文字訊息給 AI 助理

- 上傳語音檔案，使用 Faster Whisper 將語音轉換成文字

- 使用 Edge TTS 將 AI 回覆轉換成語音

- 使用 OpenAI 提供的模型處理使用者對話

- 提供文字與語音客服相關的 REST API

- 支援 Multipart File Upload，可接收使用者上傳的音訊檔案

## <br/> <a name="tech-stack">⚙️ 技術堆疊</a>

- Python
- uvicorn [📄](https://uvicorn.dev/)
- fastapi [📄](https://fastapi.tiangolo.com/)
- faster-whisper
- openai [📄](https://openai.com/)
- edge-tts [📄](https://edge-tts.com/)
- SQLAlchemy [📄](https://www.sqlalchemy.org/=)
- MySQL [📄](https://www.mysql.com/)

## <br/> <a name="quick-start">🚀 快速入門</a>

請依照以下步驟在您的電腦本機設定專案：

<br/>**必備條件**

確保您的電腦已安裝以下軟體：

- [Python](https://www.python.org/downloads/)
- [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows) | [Visual Studio Code](https://code.visualstudio.com/download?_exp_download=d53503e735)
- [MySQL](https://www.mysql.com/downloads/)
- [Git](https://git-scm.com/)

<br/>**複製儲存庫**

```bash
git clone {git remote url}
```

<br/>**建立虛擬環境**

```bash
python -m venv .venv
```

<br/>**安裝專案相依套件**

```bash
pip install -e .
```

<br/>**建立 .env**

以下是如何複製 .env.example 並在您的電腦上建立新的 .env：

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

<br/>**啟動應用程式**

安裝完所有內容並設定 .env 後，請執行：

```bash
uvicorn app.main:app --reload
```

開啟 http://127.0.0.1:8000/docs ，確認所有 API 是否都有在 Swagger 中顯示。如果都有，表示您的環境應該已經設定正確。
