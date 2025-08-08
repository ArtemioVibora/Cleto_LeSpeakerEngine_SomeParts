from gtts import gTTS
import pygame as pg
from io import BytesIO

class ChatEngine:
    """A simple chat engine that uses text-to-speech for responses."""

    def __init__(self):
        pg.init()
        pg.mixer.init()

        self.speak_text = "Hello""
        self.voice = BytesIO()
        tts = gTTS(self.speak_text, lang='tl')
        tts.write_to_fp(self.voice)

        self.voice.seek(0)
        self.sound = pg.mixer.Sound(self.voice)

    def __init__(self, type=None):
        pg.init()
        pg.mixer.init()

        self.type = type
        self.speak_text = "Hello!"
        self.voice = BytesIO()
        tts = gTTS(self.speak_text, lang='tl')
        tts.write_to_fp(self.voice)

        self.voice.seek(0)
        self.sound = pg.mixer.Sound(self.voice)

    def speak(self):
        self.sound.play()
        while pg.mixer.get_busy():
            pg.time.Clock().tick(10)

    def say(self, text):
        self.speak_text = text
        self.voice = BytesIO()
        tts = gTTS(self.speak_text, lang='tl')
        tts.write_to_fp(self.voice)

        self.voice.seek(0)
        self.sound = pg.mixer.Sound(self.voice)
        self.speak()

    def greet(self):
        self.greet_text = "Welcome to the le Chatbot!"
        self.greet_voice = BytesIO()
        greet_tts = gTTS(self.greet_text, lang='tl')
        greet_tts.write_to_fp(self.greet_voice)

        self.greet_voice.seek(0)
        self.greet_sound = pg.mixer.Sound(self.greet_voice)
        self.greet_sound.play()

    def stop(self):
        pg.mixer.stop()

    def run(self):
        self.speak()
        pg.quit()
