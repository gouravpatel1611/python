from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.lang import Builder
from kivymd.uix.taptargetview import MDTapTargetView


KV = '''

ScreenManager: 
    Hello:
    Bey:

<Hello>:
    name: 'hlo'
    MDIconButton:
        icon: 'android'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        user_font_size: '150sp'
        on_press: app.open_target()
        on_release : root.manager.current = 'by'
        
    
        
<Bey>:
    name: 'by'
    MDFloatingActionButton:
        id: textview
        icon:'plus'
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size: '45sp'
        on_press: app.close_target()
        
        
        
        
        

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
        self.target_view = MDTapTargetView(
            widget = self.scr.get_screen('by').ids.textview,
            title_text = "This is a button",
            description_text="This is a description of the button",
            widget_position="left_bottom",

        )
        return screen
    def open_target(self):
        self.target_view.start()
    def close_target(self):
        self.target_view.stop()
Demo().run()