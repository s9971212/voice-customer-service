import logging

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

        self.system_messages = [
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
            },
        ]

        self.conversation_messages = []

    def ask(self, message):
        """
        問題或指令
        """

        self._trim_messages()

        self.conversation_messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        messages = self.system_messages + self.conversation_messages

        with self.client.responses.stream(
                model="gpt-5",
                input=messages,
        ) as stream:
            full_text = ""

            for event in stream:
                if event.type == "response.output_text.delta":
                    full_text += event.delta

            final_response = stream.get_final_response()

        self._add_assistant(full_text)

        logger.info(
            "OpenAI token 使用量: %s",
            final_response.usage,
        )

        return full_text

    def _add_assistant(self, message):
        """
        添加 AI 過去生成過的回應
        """

        self.conversation_messages.append(
            {
                "role": "assistant",
                "content": message
            }
        )

    def _trim_messages(self):
        """
        保留最近 N 個回應
        """

        if len(self.conversation_messages) > settings.max_conversation_messages:
            self.conversation_messages = self.conversation_messages[-settings.max_conversation_messages:]
