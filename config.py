"""
Configuration settings for the Real Estate Research Tool
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = Path(__file__).parent
RESOURCES_DIR = BASE_DIR / "Resources"
VECTORSTORE_DIR = RESOURCES_DIR / "vectorstore"

# Ensure directories exist
VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# Model Configuration
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
MAX_TOKENS = 500
TEMPERATURE = 0.9

# Vector Store Configuration
COLLECTION_NAME = "real_estate"
MAX_TOKENS_LIMIT = 8000
RETRIEVER_K = 4

# Validation
def validate_config():
    """Validate that all required configuration is present"""
    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY environment variable is required. "
            "Please add it to your .env file."
        )
    
    return True 