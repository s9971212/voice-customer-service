from fastapi import APIRouter, Form, UploadFile, File
from fastapi.responses import Response

from ..schemas.chat import (
    ChatRequest,
    ChatResponse,
)
from ..session.manager import SessionManager
from ..voice.asr_whisper import WhisperASR
from ..voice.text_to_speech import TextToSpeech

router = APIRouter()

session_manager = SessionManager()

whisper = WhisperASR()
tts = TextToSpeech()


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    """
    文字詢問 ChatGPT
    """

    gpt = session_manager.get_session(payload.session_id)
    response_text = gpt.ask(payload.message)

    return {
        "reply": response_text
    }


@router.post("/voice-chat")
async def voice_chat(
        session_id: str = Form(...),
        audio: UploadFile = File(...),
):
    """
    語音詢問 ChatGPT
    """

    gpt = session_manager.get_session(session_id)

    processed_audio, text = whisper.transcribe(audio.file)

    response_text = gpt.ask(text)

    audio_data = await tts.generate(response_text)

    return Response(
        content=audio_data,
        media_type="audio/mpeg",
        headers={
            "X-Transcript": text,
            "X-Response-Text": response_text,
        },
    )
