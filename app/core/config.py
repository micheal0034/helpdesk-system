# app/core/config.py
import os
from dotenv import load_dotenv

# Load from .env at project root
load_dotenv()

class Settings:
    AZURE_DEPLOYMENT_NAME: str = os.getenv("AZURE_DEPLOYMENT_NAME")
    AZURE_OPENAI_KEY: str = os.getenv("AZURE_OPENAI_KEY")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_NAME: str = os.getenv("AZURE_OPENAI_NAME", "AzureAI")
    AZURE_OPENAI_API_VERSION: str = os.getenv("AZURE_OPENAI_API_VERSION")

    INDEX_PATH: str = os.getenv("INDEX_PATH", "data/faiss.index")
    CATEGORIES_PATH: str = os.getenv("CATEGORIES_PATH", "app/models/categories.json")
    DATA_DIR: str = os.getenv("DATA_DIR", "uploads")

settings = Settings()

required_keys = [
    ("AZURE_DEPLOYMENT_NAME", settings.AZURE_DEPLOYMENT_NAME),
    ("AZURE_OPENAI_KEY", settings.AZURE_OPENAI_KEY),
    ("AZURE_OPENAI_ENDPOINT", settings.AZURE_OPENAI_ENDPOINT),
]

for key, val in required_keys:
    if not val:
        raise EnvironmentError(f"Missing required config: {key}")