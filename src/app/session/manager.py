from typing import Dict

from ..llm.openai_client import ChatGPTClient


class SessionManager:

    def __init__(self):

        # =========================
        # Session
        # =========================

        self.sessions: Dict[str, ChatGPTClient] = {}

    def get_session(self, session_id):
        """
        取得 Session
        """

        if session_id not in self.sessions:
            self.sessions[session_id] = ChatGPTClient()

        return self.sessions[session_id]

    def delete_session(self, session_id):
        """
        刪除 Session
        """

        self.sessions.pop(session_id, None)

    def has_session(self, session_id):
        """
        Session 是否存在
        """

        return session_id in self.sessions
