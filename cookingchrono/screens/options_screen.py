from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<OptionsScreen>
    name: "OptionsScreen"
    MDLabel:
        text: "Options"
        pos_hint: {"center_x": .5, "center_y": .80}
        valign: 'middle'
        halign: 'center'
""")


class OptionsScreen(MDScreen):
    pass
