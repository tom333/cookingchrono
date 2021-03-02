from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivymd.uix.list import OneLineIconListItem

Builder.load_string(
    """
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color
"""
)


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))

    def __init__(self, dest_screen_name, **kwargs):
        super().__init__(**kwargs)
        self.dest_screen_name = dest_screen_name

    def on_press(self):
        App.get_running_app().manager.current = self.dest_screen_name
        App.get_running_app().nav_drawer.set_state("close")
