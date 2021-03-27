from kivy.app import App
from kivy.core.audio import SoundLoader


class SoundPlayer:
    def __init__(self):
        self.sound = SoundLoader.load(App.get_running_app().config.get("notification", "file"))
        if self.sound:
            self.sound.volume = App.get_running_app().config.get("notification", "volume")
        self.is_playing = False

    def play(self):
        if self.sound:
            self.is_playing = True
            print("Sound found at %s" % self.sound.source)
            print("Sound is %.3f seconds" % self.sound.length)
            self.sound.play()

    def stop(self):
        if self.sound:
            self.is_playing = False
            print("Sound found at %s" % self.sound.source)
            print("Sound is %.3f seconds" % self.sound.length)
            self.sound.stop()
