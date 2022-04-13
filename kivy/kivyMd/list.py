from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.lang import Builder
from kivymd.uix.list import MDList , OneLineListItem , TwoLineListItem, ThreeLineListItem



KV = '''

ScreenManager: 
    Hello:

<Hello>:
    name: 'hlo'
    ScrollView:
        MDList:
            id: ls
            # OneLineListItem:
            #     text: "hello"
            # TwoLineListItem:
            #     text: "secondary Item"
            #     secondary_text: "halo aapka swagat hai"
            # ThreeLineListItem:
            #     text: "three Item"
            #     secondary_text: "3rd item"
            #     tertiary_text: "chalo chalte hai"
                
            
    
    

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
    
    def on_start(self):
        for i in range(21):
            self.scr.get_screen('hlo').ids.ls.add_widget(
                OneLineListItem(text = f'Item {i}')
            )
            self.scr.get_screen('hlo').ids.ls.add_widget(
                TwoLineListItem(text = f'Item {i}',secondary_text=f'discreption{i}')
            )
Demo().run()