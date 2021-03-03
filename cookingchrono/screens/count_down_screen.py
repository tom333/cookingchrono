import datetime

from kivy import Logger
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.uix.screen import MDScreen
from screens import ScreenFactory

Builder.load_string(
    """
<CountDownScreen>
    name: "CountDownScreen"

    MDLabel:
        text: "Chronomètre"
        pos_hint: {"center_x": .5, "center_y": .80}
        valign: 'middle'
        halign: 'center'
    MDLabel:
        id: timerlabel
        pos_hint: {"center_x": .5, "center_y": .5}
        valign: 'middle'
        halign: 'center'
    MDRectangleFlatButton:
        text: "Stop"
        pos_hint: {"center_x": .5, "center_y": .25}
        on_press: root.pause_count_down()

"""
)


@ScreenFactory.register("CountDownScreen")
class CountDownScreen(MDScreen):
    duration = NumericProperty(0)

    def pause_count_down(self):
        pass

    def start_timer(self):
        Logger.debug("start_timer")
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, *args):
        self.duration -= 1
        self.ids.timerlabel.text = self._convert_duration_to_mask()
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
