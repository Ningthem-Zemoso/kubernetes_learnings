from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/products_db")
    API_V1_STR: str = "/api/v1"

    model_config = {
        "env_file": ".env"
    }

settings = Settings()