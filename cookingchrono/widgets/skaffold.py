from kivy import Logger
from kivy.uix.screenmanager import Screen
from kivymd.uix.navigationdrawer import NavigationLayout, MDNavigationDrawer
from kivymd.uix.toolbar import MDToolbar

from screens import AppScreenManager
from widgets.navigation.contentnavigationdrawer import ContentNavigationDrawer


class Skaffold(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        Logger.debug(kw)
        tool_bar = MDToolbar(pos_hint={"top": 1}, elevation=10, title="Chronomètre de cuisine")
        nav_layout = NavigationLayout(x=tool_bar.height)
        sm = AppScreenManager()
        nav_layout.add_widget(sm)
        nav_drawer = MDNavigationDrawer()
        content_nav_drawer = ContentNavigationDrawer()
        content_nav_drawer.screen_manager = sm
        content_nav_drawer.nav_drawer = nav_drawer

        nav_drawer.add_widget(content_nav_drawer)
        nav_layout.add_widget(nav_drawer)

        tool_bar.left_action_items = [["menu", lambda x: nav_drawer.set_state("open")]]
        self.add_widget(tool_bar)
        self.add_widget(nav_layout)
        Logger.debug("skaffold done")
