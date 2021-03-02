from typing import Callable

from kivy import Logger
from kivy.app import App
from kivymd.uix.screen import MDScreen


class ScreenFactory:
    """ The factory class for creating screens"""

    registry = {}
    """ Internal registry for available screens """

    @classmethod
    def register(cls, name: str, icon: str = "", text: str = "", default: bool = False) -> Callable:
        """Class method to register MDScreen class to the internal registry.
        Args:
            name (str): The name of the screen.
            default (bool): Is default screen
        Returns:
            The Screen class itself.
        """
        Logger.debug("register %s " % name)

        def inner_wrapper(wrapped_class: MDScreen) -> Callable:
            if name in cls.registry:
                Logger.warning("Screen %s already exists. Will replace it", name)
            cls.registry[name] = (wrapped_class, {"default": default, "icon": icon, "text": text})
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

        for name in cls.registry:
            screen_class = cls.registry[name]
            screen = screen_class[0](**kwargs)
            if screen_class[1]["default"]:
                default_screen = screen
            #Logger.debug(App.get_running_app().menu_list)
            App.get_running_app().manager.add_widget(screen)

        if default_screen is not None:
            Logger.debug("set default_screen : %s " % default_screen.name)
            App.get_running_app().manager.current = default_screen.name
