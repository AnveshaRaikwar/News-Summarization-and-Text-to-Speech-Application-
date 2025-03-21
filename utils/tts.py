from gtts import gTTS
import time
from deep_translator import GoogleTranslator

def translate_to_hindi(text):
    return GoogleTranslator(source='auto', target='hi').translate(text)

def generate_tts(text):
    hindi_text = translate_to_hindi(text)  # Translate before converting to speech
    filename = "output.mp3"
    tts = gTTS(text=hindi_text, lang="hi")
    tts.save(filename)
    return filename