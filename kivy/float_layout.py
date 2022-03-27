from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

Window.clearcolor=(1,1,1,1)
class TestApp(App):
    def build(self):
        layout = FloatLayout()#( anchor_x="right", anchor_y="bottom")
        btn1 = Button(text="Mybtn", size_hint=(None,None),width=100, pos_hint={"center_x":0.5,"center_y":0.6})
        layout.add_widget(btn1)
        return  layout

TestApp().run()