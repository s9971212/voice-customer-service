from fastapi import APIRouter

from ..llm.openai_client import ChatGPTClient
from ..schemas.chat import (
    ChatRequest,
    ChatResponse,
)

router = APIRouter()
gpt = ChatGPTClient()


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    """
    文字詢問 ChatGPT
    """

    response = gpt.ask(payload.message)

    return {
        "reply": response
    }
