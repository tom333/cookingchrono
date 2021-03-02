from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from screens.screen_factory import ScreenFactory

Builder.load_string(
    """
<OptionsScreen>
    name: "OptionsScreen"
    MDLabel:
        text: "Options"
        pos_hint: {"center_x": .5, "center_y": .80}
        valign: 'middle'
        halign: 'center'
"""
)


@ScreenFactory.register("OptionsScreen", menu={"icon": "settings", "text": "Options"})
class OptionsScreen(MDScreen):
    pass
