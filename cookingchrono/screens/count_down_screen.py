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
        font_size: 150
        theme_text_color: "Primary"
    MDIconButton:
        id: pausebutton
        icon : "pause-circle-outline"
        pos_hint: {"center_x": .5, "center_y": .10}
        user_font_size: "64sp"
        on_press: root.pause_count_down()

"""
)


@ScreenFactory.register("CountDownScreen")
class CountDownScreen(MDScreen):
    duration = NumericProperty(0)
    count_down = None
    running = True
    def pause_count_down(self):
        Logger.debug("pause_count_down %s " %  self.count_down)
        if self.running:
            App.get_running_app().sound_player.stop()
            self.count_down.cancel()
            self.running = False
            self.ids.pausebutton.icon = "play-circle-outline"
        else:
            self.start_timer()

    def start_timer(self):
        Logger.debug("start_timer")
        self.running = True
        self.count_down = Clock.schedule_interval(self.update_timer, 1)
        self.ids.pausebutton.icon = "pause-circle-outline"

    def update_timer(self, *args):
        self.duration -= 1
        self.ids.timerlabel.text = self._convert_duration_to_mask()
        self.ids.pausebutton.icon = "pause-circle-outline"
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
