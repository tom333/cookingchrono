from garden.screens.screen_manager import AppScreenManager
from garden.widgets.navigation.contentnavigationdrawer import ContentNavigationDrawer
from kivy import Logger
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivymd.uix.toolbar import MDToolbar


class Skaffold(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Logger.debug("Skaffold init %s " % kw)
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

        App.get_running_app().menu_list = content_nav_drawer.ids.md_list
        App.get_running_app().nav_drawer = nav_drawer

        Logger.debug("skaffold done")
