from gtts import gTTS
import pygame as pg
from io import BytesIO
import threading

class ChatEngine:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.lang = 'tl'  # Default language

    def _text_to_sound(self, text):
        voice = BytesIO()
        gTTS(text, lang=self.lang).write_to_fp(voice)
        voice.seek(0)
        return pg.mixer.Sound(voice)

    def say(self, text):
        def play():
            try:
                sound = self._text_to_sound(text)
                sound.play()
                
                while pg.mixer.get_busy():
                    pg.time.Clock().tick(10)
            except Exception as e:
                print(f"[TTS Error] {e}")

        threading.Thread(target=play, daemon=True).start()

    def greet(self):
        self.say("Hello How are you")

    def stop(self):
        pg.mixer.stop()

    def run(self):
        pg.quit()
