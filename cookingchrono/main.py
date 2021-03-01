import logging
import os

from kivy import Logger
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from tinydb import TinyDB

from screens.screen_factory import ScreenFactory

Logger.setLevel(logging.DEBUG)


class CookingChronoApp(MDApp):
    manager = ObjectProperty(None)

    def build(self):
        self.theme_cls.theme_style = "Dark"

        dirname = os.path.dirname(os.path.abspath(__file__))
        self.db = TinyDB(os.path.join(dirname, "db", "db.json"))
        from screens.main_screen import MainScreen
        ScreenFactory.create_screens()
        return


if __name__ == "__main__":
    CookingChronoApp().run()
