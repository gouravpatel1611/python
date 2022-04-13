from kivymd.app import MDApp
from kivymd.uix.screen import Screen

class Demo(MDApp):
    def build(self):
        screen = Screen()
        return screen
    
Demo().run()