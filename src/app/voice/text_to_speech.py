import edge_tts

from ..config import settings


class TextToSpeech:

    @staticmethod
    async def generate(text):
        """
        文字轉語音
        """

        communicate = edge_tts.Communicate(
            text=text,
            voice=settings.voice,
        )

        audio = bytearray()

        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio.extend(chunk["data"])

        return bytes(audio)
