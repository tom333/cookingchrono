import logging
import os

from garden.screens.screen_factory import ScreenFactory
from kivy import Logger, platform
from kivy.properties import ConfigParser, ObjectProperty
from kivymd.app import MDApp
from sound_player import SoundPlayer
from tinydb import TinyDB

Logger.setLevel(logging.DEBUG)
# TODO trouver un meilleur moyen d'importer automatiquement les écrans
from screens import *


class CookingChronoApp(MDApp):
    manager = ObjectProperty(None)
    db = ObjectProperty(None)
    menu_list = ObjectProperty(None)

    def request_android_permissions(self):
        """
        Since API 23, Android requires permission to be requested at runtime.
        This function requests permission and handles the response via a
        callback.
        The request will produce a popup if permissions have not already been
        been granted, otherwise it will do nothing.
        """

        def callback(permissions, results):
            """
            Defines the callback to be fired when runtime permission
            has been granted or denied. This is not strictly required,
            but added for the sake of completeness.
            """
            if all([res for res in results]):
                print("callback. All permissions granted.")
            else:
                print("callback. Some permissions refused.")

        from android.permissions import Permission, request_permissions

        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE], callback)

    def build(self):
        if platform == "android":
            print("Android detected. Requesting permissions")
            self.request_android_permissions()

        self.theme_cls.theme_style = "Dark"

        dirname = os.path.dirname(os.path.abspath(__file__))
        self.db = TinyDB(os.path.join(dirname, "db", "db.json"))
        self.config = ConfigParser()
        self.config.read(os.path.join(dirname, "db", "config.ini"))
        self.sound_player = SoundPlayer()
        ScreenFactory.create_screens()

        if platform == "android":
            os.environ["KIVY_AUDIO"] = "ffpyplayer"
            from android.permissions import Permission, request_permissions

            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
        Logger.info("################ app built ################")

        return


if __name__ == "__main__":
    CookingChronoApp().run()
