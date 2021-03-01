from kivy.tests.common import GraphicUnitTest


class AppTestCase(GraphicUnitTest):

    def test_runtouchapp(self):
        # non-integrated approach
        from kivy.app import runTouchApp
        from kivy.uix.button import Button

        CookingChronoApp().run()

        # get your Window instance safely
        from kivy.base import EventLoop
        EventLoop.ensure_window()
        window = EventLoop.window

        # your asserts
        self.assertEqual(window.children[0], button)
        self.assertEqual(
            window.children[0].height,
            window.height
        )
