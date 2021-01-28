from kivy import Logger
from kivymd.uix.textfield import MDTextField


class TimeInput(MDTextField):
    """
    widget from https://github.com/kivy/kivy/pull/6090/files
    """
    raw_value = ""
    mask = "##:##:##"
    capital = False

    def insert_text(self, substring, from_undo=False):
        Logger.debug("insert_text: %s => %s (%s)" % (self.text, substring, len(self.text)))
        s = self._format_time(substring)
        self.text = ""
        #if len(self.text) == 8:
        return super(TimeInput, self).insert_text(s, from_undo=from_undo)
        # else:
        #     return super(TimeInput, self).insert_text("", from_undo=from_undo)

    def _format_time(self, substring):
        txt = self.text
        txt = txt.replace(":", "")
        txt += substring
        txt = str(f'{int(txt):0>6}')
        txt = ":".join((txt[0 + i:2 + i] for i in range(0, len(txt), 2)))
        return txt
