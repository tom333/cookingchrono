import logging
import os

from garden.screens.screen_factory import ScreenFactory
from kivy import Logger
from kivy.properties import ObjectProperty, ConfigParser
from kivymd.app import MDApp
from tinydb import TinyDB

from sound_player import SoundPlayer

Logger.setLevel(logging.DEBUG)
# TODO trouver un meilleur moyen d'importer automatiquement les écrans
from screens import *


class CookingChronoApp(MDApp):
    manager = ObjectProperty(None)
    db = ObjectProperty(None)
    menu_list = ObjectProperty(None)

    def build(self):
        self.theme_cls.theme_style = "Dark"

        dirname = os.path.dirname(os.path.abspath(__file__))
        self.db = TinyDB(os.path.join(dirname, "db", "db.json"))
        self.config = ConfigParser()
        self.config.read(os.path.join(dirname, "db", "config.ini"))
        self.sound_player = SoundPlayer()
        ScreenFactory.create_screens()
        Logger.info("################ app built ################")

        return


if __name__ == "__main__":
    CookingChronoApp().run()
