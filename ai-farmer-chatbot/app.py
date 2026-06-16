from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import json
import os
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

# Initialize components
recognizer = sr.Recognizer()
translator = Translator()
tts_engine = pyttsx3.init()

# Configure TTS
tts_engine.setProperty('rate', 150)
tts_engine.setProperty('volume', 0.9)

# Farmer knowledge base
FARMER_KNOWLEDGE = {
    "crops": {
        "rice": {
            "season": "Kharif (June-October)",
            "soil": "Clayey soil with good water retention",
            "water": "Requires 1000-1500mm rainfall",
            "fertilizer": "NPK 120:60:60 kg/ha",
            "pests": ["Brown plant hopper", "Stem borer", "Leaf folder"],
            "diseases": ["Blast", "Bacterial blight", "Sheath blight"]
        },
        "wheat": {
            "season": "Rabi (October-March)",
            "soil": "Well-drained loamy soil",
            "water": "Requires 400-500mm rainfall",
            "fertilizer": "NPK 120:60:40 kg/ha",
            "pests": ["Aphids", "Army worm", "Termites"],
            "diseases": ["Rust", "Smut", "Powdery mildew"]
        },
        "sugarcane": {
            "season": "Year-round (12-18 months)",
            "soil": "Deep, well-drained soil",
            "water": "Requires 1500-2000mm rainfall",
            "fertilizer": "NPK 200:100:100 kg/ha",
            "pests": ["Sugarcane borer", "White grub", "Termites"],
            "diseases": ["Red rot", "Smut", "Rust"]
        }
    },
    "weather": {
        "monsoon": "June to September - Main cropping season",
        "winter": "October to February - Rabi crops",
        "summer": "March to May - Pre-monsoon preparation"
    },
    "soil_types": {
        "clay": "Good water retention, suitable for rice",
        "sandy": "Good drainage, suitable for vegetables",
        "loamy": "Best for most crops, balanced properties"
    }
}

# Indian language codes
INDIAN_LANGUAGES = {
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

def detect_language(text):
    """Detect the language of the input text"""
    try:
        detected = translator.detect(text)
        return detected.lang
    except:
        return "en"

def translate_text(text, target_lang="en"):
    """Translate text to target language"""
    try:
        if target_lang == "en":
            return text
        result = translator.translate(text, dest=target_lang)
        return result.text
    except:
        return text

def get_farmer_response(user_input, language="en"):
    """Generate response based on farmer knowledge"""
    user_input_lower = user_input.lower()
    
    # Crop-related queries
    for crop, info in FARMER_KNOWLEDGE["crops"].items():
        if crop in user_input_lower:
            response = f"Information about {crop.title()}:\n"
            response += f"• Season: {info['season']}\n"
            response += f"• Soil: {info['soil']}\n"
            response += f"• Water requirement: {info['water']}\n"
            response += f"• Fertilizer: {info['fertilizer']}\n"
            response += f"• Common pests: {', '.join(info['pests'])}\n"
            response += f"• Common diseases: {', '.join(info['diseases'])}"
            return translate_text(response, language)
    
    # Weather queries
    if any(word in user_input_lower for word in ["weather", "season", "monsoon", "rain"]):
        response = "Weather information for farming:\n"
        for season, info in FARMER_KNOWLEDGE["weather"].items():
            response += f"• {season.title()}: {info}\n"
        return translate_text(response, language)
    
    # Soil queries
    if any(word in user_input_lower for word in ["soil", "land", "earth"]):
        response = "Soil types for farming:\n"
        for soil_type, info in FARMER_KNOWLEDGE["soil_types"].items():
            response += f"• {soil_type.title()}: {info}\n"
        return translate_text(response, language)
    
    # General farming advice
    general_responses = [
        "For better crop yield, ensure proper irrigation and timely application of fertilizers.",
        "Regular soil testing helps in determining the right fertilizer mix for your crops.",
        "Crop rotation helps in maintaining soil fertility and reducing pest problems.",
        "Use organic farming methods to improve soil health and reduce chemical dependency.",
        "Monitor weather forecasts regularly to plan your farming activities accordingly."
    ]
    
    response = random.choice(general_responses)
    return translate_text(response, language)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get('message', '')
        language = data.get('language', 'en')
        
        if not user_input:
            return jsonify({'error': 'No message provided'}), 400
        
        # Detect language if not specified
        if language == 'auto':
            detected_lang = detect_language(user_input)
            language = detected_lang
        
        # Get response
        response = get_farmer_response(user_input, language)
        
        return jsonify({
            'response': response,
            'language': language,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/voice-to-text', methods=['POST'])
def voice_to_text():
    try:
        # This would typically receive audio file
        # For demo purposes, returning a placeholder
        return jsonify({
            'text': 'Voice input received',
            'language': 'en'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/text-to-speech', methods=['POST'])
def text_to_speech():
    try:
        data = request.json
        text = data.get('text', '')
        language = data.get('language', 'en')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Configure voice based on language
        voices = tts_engine.getProperty('voices')
        if language in INDIAN_LANGUAGES.values():
            # Try to find appropriate voice for Indian language
            for voice in voices:
                if language in voice.id.lower():
                    tts_engine.setProperty('voice', voice.id)
                    break
        
        # Generate speech
        tts_engine.say(text)
        tts_engine.runAndWait()
        
        return jsonify({
            'status': 'success',
            'message': 'Speech generated'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/languages', methods=['GET'])
def get_languages():
    return jsonify({
        'languages': INDIAN_LANGUAGES
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
