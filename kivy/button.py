from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)
class TestApp(App):
    def build(self):
        btn = Button(text='click Me ',
                     size_hint = (0.3,0.1) , 
                     font_size ='50sp', 
                     pos_hint={"center_x":0.5,"center_y":0.5},
                     on_press = self.on_click,
                     on_release = self.on_click_leve
                     )
        return  btn
    def on_click(self,btn):
        print("Buttn click ho gya hai ")
    def on_click_leve(self,btn):
        print("Buttn click hat gya hai ")
        

TestApp().run()
