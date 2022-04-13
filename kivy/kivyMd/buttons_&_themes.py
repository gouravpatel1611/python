from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.lang import Builder


KV = '''

ScreenManager: 
    Hello:
    Bey:

<Hello>:
    name: 'hlo'
    MDLabel:
        text: 'helo word'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,0,1,1
        font_style: 'H3'
    MDIconButton:
        icon: 'android'
        user_font_size: '50sp'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        theme_text_color: 'Custom'
        text_color: 0,0,1,1
    
    MDFloatingActionButton:
        icon: 'android'
        user_font_size: '50sp'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        theme_text_color: 'Custom'
        text_color: 0,1,0,1
        md_bg_color: 1,0,0,1
    MDRectangleFlatIconButton:
        icon: 'android'
        user_font_size: '50sp'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        theme_text_color: 'Custom'
        text_color: 0,1,0,1
        md_bg_color: 0,1,0,1
        
<Bey>:
    name: 'by'
    Label:
        text: 'tataa bye bye'
        
        

'''

class Hello(Screen):
    pass
class Bey(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Hello(name ='hlo'))
sm.add_widget(Bey(name ='by'))

class Demo(MDApp):
    def build(self):
        screen = Screen()
        scr = Builder.load_string(KV)
        screen.add_widget(scr)
        return screen
    
Demo().run()