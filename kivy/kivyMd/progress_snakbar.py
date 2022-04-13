from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.lang import Builder


KV = '''

ScreenManager: 
    Hello:

<Hello>:
    name: 'hlo'
    #:import Snackbar kivymd.uix.snackbar.Snackbar
    MDIconButton:
        icon: 'android'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        user_font_size: '40dp'
        on_press: Snackbar(text="Progress Sucsessfully").open()
        on_release:
            app.theme_changer()

    MDProgressBar:
        id: bar
        value: 40
        pos_hint: {"center_y": .01}
         

'''

class Hello(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Hello(name ='hlo'))

class Demo(MDApp):
    def build(self):
        screen = Screen()
        self.scr = Builder.load_string(KV)
        screen.add_widget(self.scr)
        return screen
    def theme_changer(self):
        self.scr.get_screen('hlo').ids.bar.value = 90
    
Demo().run()