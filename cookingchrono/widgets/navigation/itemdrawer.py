from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.list import OneLineIconListItem


Builder.load_string("""
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)


    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color
""")


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))

