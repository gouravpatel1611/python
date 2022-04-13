from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton


KV = '''

ScreenManager: 
    Hello:
    Bey:

<Hello>:
    name: 'hlo'
    MDFloatingActionButton:
        id: btn1
        icon: "arrow-left"
        md_bg_color: 0,0,1,1
        pos_hint: {'center_x':0.4,'center_y':0.5}
        on_release: app.new_btn()
        
    MDFloatingActionButton:
        id: btn2
        icon: "arrow-right"
        md_bg_color: 1,0,0,1
        pos_hint: {'center_x':0.6,'center_y':0.5}
        on_press: app.color_changer()
        # on_release: root.manager.current = 'by'
        on_release: app.screen_change()
        
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
        self.scr = Builder.load_string(KV)
        screen.add_widget(self.scr)
        self.button = MDIconButton(icon='android',pos_hint={'center_x':0.5,'center_y':0.4},user_font_size='50sp')
        return screen
    
    
    def color_changer(self):
        self.scr.get_screen('hlo').ids.btn1.md_bg_color = 0,1,0,1
    def screen_change(self):
        self.scr.get_screen('by').manager.current = 'by'
    def new_btn(self):
        self.scr.get_screen('hlo').add_widget(self.button)
Demo().run()