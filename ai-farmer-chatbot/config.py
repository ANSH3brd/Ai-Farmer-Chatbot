# Configuration file for AI Farmer Chatbot

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    # API Keys
    GOOGLE_TRANSLATE_API_KEY = os.environ.get('GOOGLE_TRANSLATE_API_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    
    # Server Configuration
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))
    
    # Speech Configuration
    SPEECH_RATE = 150
    SPEECH_VOLUME = 0.9
    
    # Supported Languages
    SUPPORTED_LANGUAGES = {
        "hindi": "hi",
        "bengali": "bn", 
        "telugu": "te",
        "marathi": "mr",
        "tamil": "ta",
        "gujarati": "gu",
        "kannada": "kn",
        "malayalam": "ml",
        "punjabi": "pa",
        "odia": "or",
        "assamese": "as",
        "english": "en"
    }
    
    # Speech Recognition Language Mapping
    SPEECH_LANG_MAP = {
        'en': 'en-US',
        'hi': 'hi-IN',
        'bn': 'bn-IN',
        'te': 'te-IN',
        'mr': 'mr-IN',
        'ta': 'ta-IN',
        'gu': 'gu-IN',
        'kn': 'kn-IN',
        'ml': 'ml-IN',
        'pa': 'pa-IN',
        'or': 'or-IN',
        'as': 'as-IN'
    }
