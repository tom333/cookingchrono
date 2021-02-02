import datetime

from kivy import Logger
from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty
from kivymd.uix.label import MDLabel


class CountDownLabel(MDLabel):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

