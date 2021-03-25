from kivy import Logger, platform
from kivy.app import App

from garden.screens.screen_factory import ScreenFactory
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.screen import MDScreen

from sound_player import SoundPlayer

Builder.load_string(
    """
<OptionsScreen>
    name: "OptionsScreen"
    BoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "Options"
            pos_hint: {"center_x": .5, "center_y": .80}
            valign: 'middle'
            halign: 'center'

        BoxLayout:
            orientation: "horizontal"
            MDLabel:
                id: sound_file_name
                text: root.file
                halign: "center"
                on_touch_down: root.play_selected_file()
            MDRoundFlatIconButton:
                text: "Open manager"
                icon: "folder"
                pos_hint: {'center_x': .5, 'center_y': .6}
                on_release: root.file_manager_open()
        BoxLayout:
            orientation: "horizontal"
            MDSlider:
                id: volume_slider
                min: 0
                max: 100
                value: root.volume
                on_value: root.save_volume(*args)
"""
)


@ScreenFactory.register("OptionsScreen", menu={"icon": "settings", "text": "Options"})
class OptionsScreen(MDScreen):
    def on_enter(self):
        Clock.schedule_once(self._init_widget)

    def _init_widget(self, arg):
        self.file_manager = MDFileManager(exit_manager=self.exit_manager, select_path=self.select_path)
        self.file_manager.ext = ['.mp3']

    def file_manager_open(self):
        if platform == "android":
            from android.storage import primary_external_storage_path
            primary_ext_storage = primary_external_storage_path()
            self.file_manager.show(primary_ext_storage)
        else:
            self.file_manager.show("/")

    def play_selected_file(self):
        sp = App.get_running_app().sound_player
        if not sp.is_playing:
            sp.play()
        else:
            sp.stop()

    def select_path(self, path):
        self.exit_manager()
        Logger.debug("selected path: %s" % path)
        App.get_running_app().config.set("notification", "file", path)
        App.get_running_app().sound_player = SoundPlayer()
        sp = App.get_running_app().sound_player
        if not sp.is_playing:
            sp.play()
        self.ids.sound_file_name.text = path
        toast(path)
        tmp = App.get_running_app().config.write()
        Logger.debug("config writed : %s " %tmp)
        return tmp

    def exit_manager(self, *args):
        self.file_manager.close()

    @property
    def file(self):
        return App.get_running_app().config.get("notification", "file")

    @property
    def volume(self):
        return float(App.get_running_app().config.get("notification", "volume"))*100

    def save_volume(self, instance, value):
        Logger.debug("%s => %s " % (str(instance), str(value)))
        App.get_running_app().config.set("notification", "volume", str(value/100))
        sp = App.get_running_app().sound_player
        if not sp.is_playing :
            sp.play()
        sp.sound.volume = value/100
        return App.get_running_app().config.write()


