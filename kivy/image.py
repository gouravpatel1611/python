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

                    
                    
                    )
        return  img

TestApp().run()