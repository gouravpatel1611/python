from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


Window.clearcolor=(1,0,0,1)
# Window.size = (330,520)

class TestApp(App):
    def build(self):
        lay = BoxLayout(orientation = "vertical",padding="150sp",spacing="50sp")
        
        self.eml = TextInput(text="Enter your Email")
        self.pas = TextInput(text="Enter your Password")
        self.submit = Button(text="Login", on_press = self.sbt)
        
        
        lay.add_widget(self.eml)
        lay.add_widget(self.pas)
        lay.add_widget(self.submit)
        return lay
    def sbt(self,btn):
        print(f"your Email is {self.eml.text} and your password is {self.pas.text} ")

TestApp().run()