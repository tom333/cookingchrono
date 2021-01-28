from kivy import Logger
from kivy.app import App
from kivymd.uix.screen import MDScreen


class MainScreen(MDScreen):

    def start_count_down(self):
        duration = self._convert_text_to_duration(self.ids.duration.text)
        Logger.debug("duration : %s" % duration)
        App.get_running_app().manager.switch_to("CountDownScreen")
        App.get_running_app().manager.current_screen.ids.timerlabel.duration = duration

    def _convert_text_to_duration(self, txt):
        """
        txt is format ##:##:##
        :return: duration in second
        """
        h, m, s = txt.split(":")
        Logger.debug("%s, %s, %s" % (h, m, s))
        return int(h) * 60 * 60 + int(m) * 60 + int(s)
