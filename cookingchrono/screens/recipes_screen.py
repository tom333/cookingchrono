from kivy import Logger
from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<RecipesScreen>
    name: "RecipesScreen"
    orientation: 'vertical'
    MDLabel:
        text: "Liste des recettes"
        valign: 'middle'
        pos_hint: {"center_x": .5, "center_y": .80}
        halign: 'center'
    MDList:
        pos_hint: {"center_x": .5, "center_y": .50}
        id: recipes_list
    MDBoxLayout:

        orientation: "horizontal"
        MDTextField:
            id: nom
            hint_text: "Nom"
            theme_text_color: "Secondary"
            size_hint_y: None
        MDSeparator:
            height: "1dp"

        TimeInput:
            hint_text: "Durée"
            id: duree
        MDIconButton:
            icon: "plus-circle-outline"
            on_press:
                root.add_recipe(self.parent)

""")


class RecipesScreen(MDScreen):

    def add_recipe(self, card):
        Logger.debug("%s => %s" % (self.ids.nom.text, self.ids.duree.text))
        App.get_running_app().db.insert({'name': self.ids.nom.text, 'time': self.ids.duree.text})

    def on_enter(self):
        for recipe in App.get_running_app().db.all():
            Logger.debug(recipe)
            self.ids.recipes_list.add_widget(TwoLineListItem(text=recipe['name'], secondary_text=recipe['time'],
                                                             on_release=self.edit_recipe))

    def edit_recipe(self, arg):
        Logger.debug("edit_recipe : %s " % arg)
