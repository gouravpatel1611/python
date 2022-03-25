from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)
class TestApp(App):
    def build(self):
        l = Label(text='Hello World',font_size = '124sp', bold = True, italic = True, color = (1,0,0,1))
        return  l

TestApp().run()