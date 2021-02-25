from kivy import Logger
from kivymd.uix.textfield import MDTextField


class TimeInput(MDTextField):
    """
    widget de saisie de durée
    """

    def insert_text(self, substring, from_undo=False):
        Logger.debug("insert_text: %s => %s (%s)" % (self.text, substring, len(self.text)))
        s = self._format_time(substring)
        self.text = ""
        return super(TimeInput, self).insert_text(s, from_undo=from_undo)

    def _format_time(self, substring):
        txt = self.text
        txt = txt.replace(":", "")
        txt += substring
        txt = str(f'{int(txt):0>6}')
        txt = ":".join((txt[0 + i:2 + i] for i in range(0, len(txt), 2)))
        return txt
