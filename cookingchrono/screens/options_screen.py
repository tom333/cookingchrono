from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.settings import SettingsWithSpinner
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.screen import MDScreen
from screens import ScreenFactory

Builder.load_string(
    """
<OptionsScreen>
    name: "OptionsScreen"

    FloatLayout:

        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {'center_x': .5, 'center_y': .6}
            on_release: root.file_manager_open()
""")


@ScreenFactory.register("OptionsScreen", menu={"icon": "settings", "text": "Options"})
class OptionsScreen(MDScreen):
    def on_enter(self):
        Clock.schedule_once(self._init_widget)

    def _init_widget(self, arg):
        self.manager_open = False
        self.add_widget(SettingsWithSpinner())
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path
        )

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

