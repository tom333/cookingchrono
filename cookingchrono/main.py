import logging
import os

from garden.screens.screen_factory import ScreenFactory
from kivy import Logger
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from tinydb import TinyDB

Logger.setLevel(logging.DEBUG)
# TODO trouver un meilleur moyen d'importer automatiquement les écrans
from screens import *

json = """
[
    {
        "type": "string",
        "title": "Label caption",
        "desc": "Choose the text that appears in the label",
        "section": "My Label",
        "key": "text"
    },
    {
        "type": "numeric",
        "title": "Label font size",
        "desc": "Choose the font size the label",
        "section": "My Label",
        "key": "font_size"
    }
]
"""


class CookingChronoApp(MDApp):
    manager = ObjectProperty(None)
    db = ObjectProperty(None)
    menu_list = ObjectProperty(None)

    def build(self):
        self.theme_cls.theme_style = "Dark"

        dirname = os.path.dirname(os.path.abspath(__file__))
        self.db = TinyDB(os.path.join(dirname, "db", "db.json"))

        ScreenFactory.create_screens()
        return

    def build_config(self, config):
        """
        Set the default values for the configs sections.
        """
        config.setdefaults("My Label", {"text": "Hello", "font_size": 20})

    def build_settings(self, settings):
        """
        Add our custom section to the default configuration object.
        """
        # We use the string defined above for our JSON, but it could also be
        # loaded from a file as follows:
        #     settings.add_json_panel('My Label', self.config, 'settings.json')
        settings.add_json_panel("My Label", self.config, data=json)

    def on_config_change(self, config, section, key, value):
        """
        Respond to changes in the configuration.
        """
        Logger.info("main.py: App.on_config_change: {0}, {1}, {2}, {3}".format(config, section, key, value))

        if section == "My Label":
            if key == "text":
                self.root.ids.label.text = value
            elif key == "font_size":
                self.root.ids.label.font_size = float(value)


if __name__ == "__main__":
    CookingChronoApp().run()
