from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

Window.clearcolor=(1,0,0,1)
Window.size = (330,520)


class TestApp(App):
    def build(self):
        layout = GridLayout(cols=2 , col_force_default =True,col_default_width =150) # GridLayout(rows=2)
        
        btn1 = Button(text='click Me1 ')
        btn2 = Button(text='click Me 2')
        btn3 = Button(text='click Me3 ')
        btn4 = Button(text='click Me4')
        btn5 = Button(text='click Me 5')
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        
        return  layout
    
        

TestApp().run()
