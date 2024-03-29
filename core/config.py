from pathlib import PurePath
from pydantic_settings import BaseSettings, SettingsConfigDict
from settings import ROOT_DIR


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(PurePath(ROOT_DIR, ".env")), env_file_encoding="utf-8"
    )
    bot_token: str
    max_video_size: int


config = Settings()
