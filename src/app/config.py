from pathlib import Path

from pydantic import AnyHttpUrl, BeforeValidator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Annotated

# 專案根目錄
BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    # =========================
    # Pydantic Settings
    # =========================

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )

    # =========================
    # Application
    # =========================

    project_name: str = "Voice Customer Service"

    description: str = "A tool for Voice Customer Service"

    version: str = "0.1.0"

    # =========================
    # CORS
    # =========================

    backend_cors_origins: Annotated[
        list[AnyHttpUrl],
        BeforeValidator(
            lambda v: [x.strip() for x in v.split(",")]
            if isinstance(v, str)
            else v
        )
    ] = []

    # =========================
    # Database
    # =========================

    db_host: str = ""
    db_port: int = 1433
    db_name: str = ""
    db_user: str = ""
    db_password: str = ""

    # =========================
    # ChatGPT
    # =========================

    openai_api_key: str = ""

    max_messages: int = 30

    # =========================
    # Api
    # =========================

    api_v1_str: str = "/api"

    # =========================
    # Log
    # =========================

    log_path: Path = BASE_DIR / "logs" / "app.log"


settings = Settings()
