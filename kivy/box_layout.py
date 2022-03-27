from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.clearcolor=(1,0,0,1)
Window.size = (330,520)


class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical",spacing ="10sp", padding="50sp")
        
        btn1 = Button(text='click Me1 ')
        btn2 = Button(text='click Me 2')
        btn3 = Button(text='click Me3 ')
        btn4 = Button(text='click Me4')
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return  layout
    
        

TestApp().run()
