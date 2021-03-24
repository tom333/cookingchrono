from typing import Callable

from garden.widgets.navigation.itemdrawer import ItemDrawer
from kivy import Logger
from kivy.app import App
from kivymd.uix.screen import MDScreen


class ScreenFactory:
    """ The factory class for creating screens"""

    """ Internal registry for available screens """
    registry = {}

    @classmethod
    def register(cls, name: str, menu: {} = None, default: bool = False) -> Callable:
        """Class method to register MDScreen class to the internal registry.
        Args:
            name (str): The name of the screen.
            default (bool): Is default screen
            menu (dict): Menu options if needed
        Returns:
            The Screen class itself.
        """
        Logger.debug("register %s " % name)

        def inner_wrapper(wrapped_class: MDScreen) -> Callable:
            if name in cls.registry:
                Logger.warning("Screen %s already exists. Will replace it", name)
            cls.registry[name] = (wrapped_class, {"default": default, "menu": menu})
            return wrapped_class

        return inner_wrapper

    @classmethod
    def create_screens(cls, **kwargs) -> "MDScreen":
        """Factory command to create the executor.
        This method gets the appropriate Executor class from the registry
        and creates an instance of it, while passing in the parameters
        given in ``kwargs``.
        Returns:
            An instance of the executor that is created.
        """
        default_screen = None
        for name in cls.registry:
            screen_class = cls.registry[name]
            screen = screen_class[0](**kwargs)
            if screen_class[1]["default"]:
                default_screen = screen
            App.get_running_app().manager.add_widget(screen)
            if screen_class[1]["menu"] is not None:
                Logger.debug("ajout du menu %s " % screen_class[1]["menu"]["text"])
                menu_item = ItemDrawer(icon=screen_class[1]["menu"]["icon"], text=screen_class[1]["menu"]["text"], dest_screen_name=screen.name)
                App.get_running_app().menu_list.add_widget(menu_item)

        if default_screen is not None:
            Logger.debug("set default_screen : %s " % default_screen.name)
            App.get_running_app().manager.current = default_screen.name
