import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings:
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "3306"))
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "ppo_trading")

    MODEL_DIR: str = os.getenv("MODEL_DIR", "ai/models/")

    class Config:
        case_sensitive = True

settings = Settings()