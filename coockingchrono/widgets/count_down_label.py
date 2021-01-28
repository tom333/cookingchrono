import datetime

from kivy import Logger
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty
from kivymd.uix.label import MDLabel


class CountDownLabel(MDLabel):
    duration = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        self.duration -= 1
        self.text = self._convert_duration_to_mask()
        if self.duration == 0:
            self._play_sound()

    def _play_sound(self):
        Logger.debug("play sound")
        sound = SoundLoader.load("../assets/sound.mp3")
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    def _convert_duration_to_mask(self):
        Logger.debug("timer: %s " % self.duration)
        return str(datetime.timedelta(seconds=self.duration))
