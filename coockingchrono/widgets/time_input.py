from kivy import Logger
from kivymd.uix.textfield import MDTextField


class TimeInput(MDTextField):
    """
    widget from https://github.com/kivy/kivy/pull/6090/files
    """
    mask = '##:##:##'
    capital = False

    def insert_text(self, substring, from_undo=False):
        first = False
        s = ''
        if self.mask == '':
            s = substring
        else:
            mask = self.mask
            col, row = self.cursor
            if col < len(mask):
                if mask[col] == '#':
                    numbers = '1234567890'
                    if substring in numbers:
                        s = substring
                elif mask[col] == 'A':
                    letters = 'QWERTYUIOPASDFGHJKLÇZXCVBNMqwertyuiopasdfghjklçzxcvbnm'
                    if substring in letters:
                        s = substring
                elif mask[col] == substring:
                    s = substring
                else:
                    s = mask[col]
                    first = True
                if col < len(mask) - 1:
                    if mask[col + 1] != '#' and mask[col + 1] != 'A':
                        s += mask[col + 1]
                    if first:
                        s += substring

        if self.capital:
            s = substring.upper()

        return super(TimeInput, self).insert_text(s, from_undo=from_undo)