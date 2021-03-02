from kivy import Logger
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_string(
    """
#:import DrawerList widgets.navigation.drawerlist
#:import ItemDrawer widgets.navigation.itemdrawer

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: home.height

        MDIconButton:
            id: home
            ico: "home"
            user_font_size: "56sp"

    MDLabel:
        text: "Chronomètre de cuisine"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list
"""
)


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.debug(ContentNavigationDrawer)
        Clock.schedule_once(lambda *args: self._register_menu_list())

    def _register_menu_list(self):
        Logger.debug("_register_menu_list")
        App.get_running_app().menu_list = self.ids.md_list
