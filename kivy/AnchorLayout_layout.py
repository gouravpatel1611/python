from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout

Window.clearcolor=(1,1,1,1)
class TestApp(App):
    def build(self):
        layout = AnchorLayout( anchor_x="right", anchor_y="bottom")
        btn1 = Button(text="Mybtn", size_hint=(None,None),width=100)
        layout.add_widget(btn1)
        return  layout

TestApp().run()