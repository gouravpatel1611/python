from kivy.app import App
from kivy.uix.image import Image , AsyncImage
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)
class TestApp(App):
    def build(self):
        img = Image(
                    source='kanad.gif',
                     size_hint = (None,None),
                     width = 500,
                     height = 200,
                     pos_hint={"left":0.1,"top":1},

                    
                    
                    )
        return  img

TestApp().run()