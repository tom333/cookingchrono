import logging

from kivy import Logger
from kivy.properties import ObjectProperty

from kivymd.app import MDApp

from screens.count_down_screen import CountDownScreen
from screens.main_screen import MainScreen
from screens.screen_manager import AppScreenManager

Logger.setLevel(logging.DEBUG)


class CookingChronoApp(MDApp):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = AppScreenManager()
        self.manager.add_widget(MainScreen(name="MainScreen"))
        self.manager.add_widget(CountDownScreen(name="CountDownScreen"))
        self.theme_cls.theme_style = "Dark"
        return self.manager


if __name__ == "__main__":
    CookingChronoApp().run()
