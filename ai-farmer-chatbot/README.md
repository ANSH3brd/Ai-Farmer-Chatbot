# AI Farmer Chatbot

A multilingual AI-powered farming assistant that supports Indian languages and voice interaction.

## Features

- 🌾 **Farming Knowledge Base**: Comprehensive information about crops, weather, soil, and farming techniques
- 🗣️ **Voice Assistant**: Speech-to-text and text-to-speech capabilities
- 🌍 **Multilingual Support**: Supports 12 Indian languages including Hindi, Bengali, Telugu, Marathi, Tamil, and more
- 💬 **Interactive Chat**: Modern, responsive chat interface
- 📱 **Mobile Friendly**: Works on desktop and mobile devices

## Supported Languages

- English (en)
- Hindi (hi) - हिन्दी
- Bengali (bn) - বাংলা
- Telugu (te) - తెలుగు
- Marathi (mr) - मराठी
- Tamil (ta) - தமிழ்
- Gujarati (gu) - ગુજરાતી
- Kannada (kn) - ಕನ್ನಡ
- Malayalam (ml) - മലയാളം
- Punjabi (pa) - ਪੰਜਾਬੀ
- Odia (or) - ଓଡ଼ିଆ
- Assamese (as) - অসমীয়া

## Installation

1. Clone or download this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://localhost:5000`

## Usage

### Text Chat
- Type your farming questions in the chat input
- Select your preferred language from the dropdown
- Click the send button or press Enter

### Voice Interaction
- Click the microphone button to start voice recording
- Speak your question in your preferred language
- The assistant will respond with both text and voice

### Quick Questions
Use the quick action buttons for common farming queries:
- Rice Cultivation
- Wheat Season
- Soil Quality
- Weather Advice
- Pest Control

## API Endpoints

- `POST /api/chat` - Send a message to the chatbot
- `POST /api/voice-to-text` - Convert voice to text
- `POST /api/text-to-speech` - Convert text to speech
- `GET /api/languages` - Get supported languages

## Knowledge Base

The chatbot includes information about:

### Crops
- Rice, Wheat, Sugarcane
- Growing seasons, soil requirements
- Water needs, fertilizer recommendations
- Common pests and diseases

### Weather
- Seasonal farming advice
- Monsoon, winter, and summer guidance

### Soil Types
- Clay, sandy, and loamy soils
- Best crops for each soil type

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Speech Recognition**: Web Speech API
- **Text-to-Speech**: Web Speech Synthesis API
- **Translation**: Google Translate API
- **Styling**: Modern CSS with responsive design

## Browser Compatibility

- Chrome (recommended for best voice support)
- Firefox
- Safari
- Edge

## Contributing

Feel free to contribute by:
- Adding more crops and farming knowledge
- Improving language support
- Enhancing the user interface
- Adding new features

## License

This project is open source and available under the MIT License.
