from typing import Callable

from kivy import Logger
from kivymd.uix.screen import MDScreen


class ScreenFactory:
    """ The factory class for creating screens"""

    registry = {}
    """ Internal registry for available screens """

    @classmethod
    def register(cls, name: str) -> Callable:
        """ Class method to register MDScreen class to the internal registry.
        Args:
            name (str): The name of the screen.
        Returns:
            The Screen class itself.
        """

        def inner_wrapper(wrapped_class: MDScreen) -> Callable:
            if name in cls.registry:
                Logger.warning('Screen %s already exists. Will replace it', name)
            cls.registry[name] = wrapped_class
            return wrapped_class

        return inner_wrapper

    # end register()

    @classmethod
    def create_screens(cls, **kwargs) -> 'MDScreen':
        """ Factory command to create the executor.
        This method gets the appropriate Executor class from the registry
        and creates an instance of it, while passing in the parameters
        given in ``kwargs``.
        Args:
            name (str): The name of the executor to create.
        Returns:
            An instance of the executor that is created.
        """
        for name in cls.registry:
            screen_class = cls.registry[name]
            screen = screen_class(**kwargs)
            Logger.debug(screen)

        return

    # end create_executor()

# end class ExecutorFactory
