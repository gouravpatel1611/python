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

    MDFloatingActionButton:
        icon: 'android'
        user_font_size: '50sp'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        theme_text_color: 'Custom'
        text_color: 0,1,0,1
        md_bg_color: 1,0,0,1
        on_release: 
            root.manager.current = 'by'
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        id: txt
        text: "DARK"
        user_font_size: '50sp'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        theme_text_color: 'Custom'
        text_color: 0,1,0,1
        md_bg_color: 0,1,0,1
        on_release:
            app.theme_changer()
    
    
        
<Bey>:
    name: 'by'
    Label:
        text: "tataa bye bye"
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
    MDIconButton:
        icon: 'android'
        user_font_size: '50sp'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        theme_text_color: 'Custom'
        text_color: 0,0,1,1
        on_release: 
            root.manager.current = 'hlo'
            root.manager.transition.direction = 'right'
        
        

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
        self.scr = Builder.load_string(KV)
        screen.add_widget(self.scr)
        return screen
    def theme_changer(self):
        print("halo")
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            self.scr.get_screen('hlo').ids.txt.text = "Dark"
        else:
            self.theme_cls.theme_style = 'Dark'
            self.scr.get_screen('hlo').ids.txt.text = "Light"
    
Demo().run()