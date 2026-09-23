from fastapi import APIRouter, UploadFile, File
from fastapi.responses import Response

from ..llm.openai_client import ChatGPTClient
from ..schemas.chat import (
    ChatRequest,
    ChatResponse,
)
from ..voice.asr_whisper import WhisperASR
from ..voice.text_to_speech import TextToSpeech

router = APIRouter()
whisper = WhisperASR()
gpt = ChatGPTClient()
tts = TextToSpeech()


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    """
    文字詢問 ChatGPT
    """

    response_text = gpt.ask(payload.message)

    return {
        "reply": response_text
    }


@router.post("/voice-chat")
async def voice_chat(
        audio: UploadFile = File(...)
):
    """
    語音詢問 ChatGPT
    """

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
