from functools import partial

from kivy import Logger
from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<MainScreen>
    name: "MainScreen"
    orientation: 'vertical'
    MDLabel:
        text: "Chronomètre"
        pos_hint: {"center_x": .5, "center_y": .80}
        valign: 'middle'
        halign: 'center'
    MDList:
        pos_hint: {"center_x": .5, "center_y": .50}
        id: recipes_list
    TimeInput:
        id: duration
        text: "00:00:00"
        max_text_length: 8
        pos_hint: {"center_x": .5, "center_y": .5}
        valign: 'middle'
        halign: 'center'
    MDIconButton:
        icon: "play-circle-outline"
        pos_hint: {"center_x": .5, "center_y": .25}
        on_press: root.start_count_down()

""")


class MainScreen(MDScreen):
    def start_count_down(self):
        duration = self._convert_text_to_duration(self.ids.duration.text)
        Logger.debug("duration : %s" % duration)
        self.manager.current = "CountDownScreen"
        self.manager.current_screen.duration = duration
        self.manager.current_screen.start_timer()

    def _convert_text_to_duration(self, txt):
        """
        txt is format ##:##:##
        :return: duration in second
        """
        h, m, s = txt.split(":")
        Logger.debug("%s, %s, %s" % (h, m, s))
        return int(h) * 60 * 60 + int(m) * 60 + int(s)

    def on_enter(self):
        self.ids.recipes_list.clear_widgets()
        for recipe in App.get_running_app().db.all():
            Logger.debug(recipe)
            self.ids.recipes_list.add_widget(TwoLineListItem(text=recipe['name'], secondary_text=recipe['time'],
                                                             on_release=partial(self.set_time, recipe.doc_id)))

    def set_time(self, id, item):
        Logger.debug("edit_recipe : %s => %s (%s) " % (item, id, self.ids))
        current_recipe = App.get_running_app().db.get(doc_id=id)
        self.ids.nom.text = current_recipe['name']
        self.ids.duration.text = current_recipe['time']
