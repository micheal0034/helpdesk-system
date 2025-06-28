# app/embedding/client.py

import numpy as np
from typing import List
from openai import AzureOpenAI
from sentence_transformers import SentenceTransformer
from app.core.config import settings

# Use local model for embeddings
_embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Optionally set up OpenAI client
AZURE_DEPLOYMENT = settings.AZURE_DEPLOYMENT_NAME
AZURE_API_KEY = settings.AZURE_OPENAI_KEY
AZURE_ENDPOINT = settings.AZURE_OPENAI_ENDPOINT
AZURE_NAME = settings.AZURE_OPENAI_NAME
AZURE_OPENAI_API_VERSION = settings.AZURE_OPENAI_API_VERSION

_client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_ENDPOINT
)

def embed_text(text: str) -> np.ndarray:
    """Embed a single piece of text using SentenceTransformers."""
    embedding = _embedding_model.encode(text)
    return np.array(embedding)

def generate_response(prompt: str) -> str:
    """Generate a response using Azure OpenAI."""
    if not AZURE_DEPLOYMENT:
        raise RuntimeError("AZURE_DEPLOYMENT_NAME is not set")
    
    completion = _client.chat.completions.create(
        model=AZURE_NAME,
        messages=[
            {"role": "system", "content": "You are an expert IT help desk assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return completion.choices[0].message.content.strip()
