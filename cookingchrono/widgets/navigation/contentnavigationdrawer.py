from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
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

            ItemDrawer:
                icon: "metronome"
                text: "Chronomètre"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "MainScreen"

            ItemDrawer:
                icon: "settings"
                text: "Options"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "OptionsScreen"

""")


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
