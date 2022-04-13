from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.lang import Builder


KV = '''

ScreenManager: 
    Hello:
<MyTile@SmartTileWithStar>
#<MyTile@SmartTileWithLabel>
    size_hint_y : None
    height: '240sp'

<Hello>:
    name: 'hlo'
    ScrollView:
        MDGridLayout:
            cols: 3
            padding: dp(4),dp(4)
            spacing: dp(8)

            MyTile:
                text: "[size=24]FaceBook[/size]"
                source: 'fb.png'
            MyTile:
                text: "[size=26][color=#FF0000]Cat 3[/color][/size]"
                source: '1.jpg'
            MyTile:
                stars:4
                source: '2.jpg'
            MyTile:
                stars:4
                source: '3.jpg'
            MyTile:
                stars:4
                source: '4.jpg'
            MyTile:
                stars:4
                source: '5.jpg'
            MyTile:
                stars:4
                source: '6.jpg'
            MyTile:
                stars:4
                source: '7.jpg'
            MyTile:
                stars:4
                source: '8.jpg'
            MyTile:
                stars:4
                source: '1.jpg'
            
    

'''

class Hello(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Hello(name ='hlo'))

class Demo(MDApp):
    def build(self):
        screen = Screen()
        scr = Builder.load_string(KV)
        screen.add_widget(scr)
        return screen
    
Demo().run()