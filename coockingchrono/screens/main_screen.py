from kivy import Logger
from kivy.core.audio import SoundLoader
from kivymd.uix.screen import MDScreen


class MainScreen(MDScreen):

    def play_sound(self):
        Logger.debug("play sound")
        sound = SoundLoader.load('../assets/sound.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
