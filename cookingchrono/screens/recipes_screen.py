from functools import partial

from garden.screens.screen_factory import ScreenFactory
from kivy import Logger
from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.screen import MDScreen

Builder.load_string(
    """
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
        id: editing
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

"""
)


@ScreenFactory.register("RecipesScreen", menu={"icon": "food", "text": "Recettes"})
class RecipesScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.current_id = None

    def add_recipe(self, card):
        Logger.debug("%s => %s" % (self.ids.nom.text, self.ids.duree.text))
        if self.current_id is not None:
            Logger.debug("mise à jour de %s " % self.current_id)
            App.get_running_app().db.update({"name": self.ids.nom.text, "time": self.ids.duree.text}, doc_ids=[self.current_id])
        else:
            Logger.debug("création")
            self.current_id = App.get_running_app().db.insert({"name": self.ids.nom.text, "time": self.ids.duree.text})
        self.on_enter()

    def on_enter(self):
        self.ids.recipes_list.clear_widgets()
        for recipe in App.get_running_app().db.all():
            Logger.debug(recipe)
            self.ids.recipes_list.add_widget(TwoLineListItem(text=recipe["name"], secondary_text=recipe["time"], on_release=partial(self.edit_recipe, recipe.doc_id)))

    def edit_recipe(self, id, item):
        Logger.debug("edit_recipe : %s => %s (%s) " % (item, id, self.ids))
        self.current_id = id
        current_recipe = App.get_running_app().db.get(doc_id=id)
        self.ids.nom.text = current_recipe["name"]
        self.ids.duree.text = current_recipe["time"]
