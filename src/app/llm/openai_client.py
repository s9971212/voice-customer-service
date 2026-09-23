import logging
from typing import Any

from openai import OpenAI

from .contexts import CONTEXT
from .prompts import PROMPT
from ..config import settings

logger = logging.getLogger(__name__)


class ChatGPTClient:

    def __init__(self):

        # =========================
        # OpenAI
        # =========================

        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

        self.history: Any = [
            {
                "role": "system",
                "content": PROMPT
            },
            {
                "role": "system",
                "content": f"""
                以下是知識庫資料：

                {CONTEXT}
                """
            }
        ]

    def ask(self, text):
        """
        問題或指令
        """

        if len(self.history) > settings.max_messages:
            self.history = self.history[:2] + self.history[-settings.max_messages:]

        self.history.append(
            {
                "role": "user",
                "content": text
            }
        )

        with self.client.responses.stream(
                model="gpt-5",
                input=self.history,
        ) as stream:
            full_text = ""

            for event in stream:
                if event.type == "response.output_text.delta":
                    full_text += event.delta

            final_response = stream.get_final_response()

        logger.info(
            "OpenAI token 使用量: %s",
            final_response.usage,
        )

        self.add_assistant(full_text)

        return full_text

    def add_assistant(self, text):
        """
        添加 AI 過去生成過的回應
        """

        if len(self.history) > settings.max_messages:
            self.history = self.history[:2]

        self.history.append(
            {
                "role": "assistant",
                "content": text
            }
        )
