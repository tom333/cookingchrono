import datetime

from garden.screens.screen_factory import ScreenFactory
from jnius import autoclass
from kivy import Logger
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.uix.screen import MDScreen
from oscpy.client import OSCClient
from oscpy.server import OSCThreadServer
from plyer import notification

Builder.load_string(
    """
<CountDownScreen>
    name: "CountDownScreen"
    MDBoxLayout:
        orientation: 'vertical'
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
        MDBoxLayout:
            orientation: 'horizontal'
            MDIconButton:
                id: reinitbutton
                icon : "reload"
                size_hint: (.5,1)
                user_font_size: "64sp"
                on_press: root.reinit_count_down()
            MDIconButton:
                id: pausebutton
                icon : "pause-circle-outline"
                size_hint: (.5,1)
                user_font_size: "64sp"
                on_press: root.pause_count_down()

"""
)


@ScreenFactory.register("CountDownScreen")
class CountDownScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.running = True
        self.duration = NumericProperty(0)
        SERVICE_NAME = "{packagename}.Service{servicename}".format(packagename="com.moi.cookingchrono", servicename="Cookingchrono")
        self.service = autoclass(SERVICE_NAME)
        self.server = OSCThreadServer()
        self.server.listen(address=b"localhost", port=3002, default=True)

        self.server.bind(b"/count_down", self.update_timer)
        self.client = OSCClient(b"localhost", 3000)

    def pause_count_down(self):
        Logger.debug("pause_count_down")
        self.client.send_message(b"/pause", [])
        if self.running:
            App.get_running_app().sound_player.stop()
            self.running = False
            self.ids.pausebutton.icon = "play-circle-outline"
        else:
            self.start_timer()

    def reinit_count_down(self):
        self.running = False
        self.duration = 0
        self.manager.current = "MainScreen"
        self.manager.current_screen.duration = 0

    def start_timer(self):
        Logger.debug("start_timer")
        self.running = True
        mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
        argument = str(self.duration)
        self.service.start(mActivity, argument)
        self.ids.pausebutton.icon = "pause-circle-outline"

    def update_timer(self, duration):
        self.duration = int(duration.decode("utf-8"))
        self.ids.timerlabel.text = self._convert_duration_to_mask()
        self.ids.pausebutton.icon = "pause-circle-outline"
        if self.duration % 60 == 0:
            notification.notify(title="Chrono en cours", message="Il reste %s " % self.ids.timerlabel.text, timeout=10)

        if self.duration == 0:
            self._play_sound()

    def _play_sound(self):
        Logger.debug("play sound")
        App.get_running_app().sound_player.play()

    def _convert_duration_to_mask(self):
        Logger.debug("timer: %s " % self.duration)
        return str(datetime.timedelta(seconds=self.duration))
