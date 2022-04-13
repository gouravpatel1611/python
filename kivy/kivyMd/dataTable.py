from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


KV = '''

ScreenManager: 
    Hello:
    Bey:

<Hello>:
    name: 'hlo'
    
        
<Bey>:
    name: 'by'
    MDLabel:
        id: txt
        text: 'tataa bye bye'
        theme_text_color: 'Custom'
        text_color: 1,0,1,1
        font_style: 'H3'
        
        

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
        
        table = MDDataTable(pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.9,0.6),check=True,rows_num=7,
                            column_data = [
                                ("food",dp(30)),
                                ("Calories",dp(30)),
                                ("Price",dp(30)),
                                ("Must Buy",dp(30)),
                            ],
                            row_data = [
                                ("Apple","3000","50","No"),
                                ("Mango","3000","50","No"),
                                ("Orange","3000","50","No"),
                                ("Banana","3000","50","No"),
                                ("Greps","3000","50","No"),
                                ("Kgf","3000","50","No"),
                                ("Best","3000","50","No"),
                            ]
                            )
        table.bind(on_check_press = self.check_press)
        table.bind(on_row_press = self.row_press)
        self.scr.get_screen('hlo').add_widget(table)
        screen.add_widget(self.scr)
        return screen
    def check_press(self, instance_table,current_row):
        self.scr.get_screen('by').ids.txt.text = current_row[0]
        self.scr.get_screen('by').manager.current = 'by'
    def row_press(self, instance_table,current_row):
        pass
    
Demo().run()