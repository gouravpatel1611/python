from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window

Window.size = (400,600)


KV = '''

ScreenManager: 
    Hello:
    Bey:

<Hello>:
    name: 'hlo'
    MDScreen:
        ScreenManager:
            MDScreen:
                MDToolbar:
                    title: "Navigation Drawer"
                    elevation: 10
                    pos_hint: {"top": 1}
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '5dp'
                padding: '5dp'
                Image:
                    size_hint_y: 0.5
                    size_hint_x: 0.5
                    source: 'fb.png'
                    pos_hint: {'center_x':0.5,'center_y':0.5}
                    
                MDLabel:
                    text: "Demo app"
                    font_style: "H5"
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Gourav"
                            IconLeftWidget:
                                icon: 'plus'
                        OneLineIconListItem:
                            text: "Rahul"
                            IconLeftWidget:
                                icon: 'android'
                        OneLineIconListItem:
                            text: "Mehul"
                            IconLeftWidget:
                                icon: 'arrow-right'
                                
                            

                    
            

                

        
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