import logging

from kivy import Logger
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivymd.app import MDApp

from screens.main_screen import MainScreen
from screens.screen_manager import AppScreenManager

Logger.setLevel(logging.DEBUG)


class CookingChronoApp(MDApp):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = AppScreenManager()
        self.manager.add_widget(MainScreen(name="MainScreen"))
        self.theme_cls.primary_palette = "BlueGray"
        return self.manager


if __name__ == "__main__":
    CookingChronoApp().run()
    #MainScreen(name="MainScreen")
