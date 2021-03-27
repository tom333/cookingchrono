import datetime

from plyer import notification

from garden.screens.screen_factory import ScreenFactory
from kivy import Logger, platform
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.uix.screen import MDScreen

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
    count_down = None

    def pause_count_down(self):
        App.get_running_app().sound_player.stop()
        self.count_down.cancel()

    def start_timer(self):
        Logger.debug("start_timer")
        self.count_down = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, *args):
        self.duration -= 1
        self.ids.timerlabel.text = self._convert_duration_to_mask()
        if self.duration % 60 == 0 :
            notification.notify(title='Chrono en cours', message='Il reste %s ' % self.ids.timerlabel.text,
                                timeout=10 )

        if self.duration == 0:
            self._play_sound()

    def _play_sound(self):
        Logger.debug("play sound")
        App.get_running_app().sound_player.play()

    def _convert_duration_to_mask(self):
        Logger.debug("timer: %s " % self.duration)
        return str(datetime.timedelta(seconds=self.duration))
