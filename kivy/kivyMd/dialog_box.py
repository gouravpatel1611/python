from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen ,ScreenManager
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


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
    MDTextField:
        id: username_text
        hint_text: 'username'
        color_mode: 'custom'
        line_color_normal: 0,1,1,1
        line_color_focus: 0,1,0,1
        helper_text: 'Required'
        helper_text_mode: "on_error"
        mode: "rectangle"
        icon_right: 'account'
        icon_right_color: 1,0,0,1
        pos_hint: {'center_x':0.5,'center_y':0.5}
        required: True
        size_hint: (0.8,0.1)
        
        

    MDIconButton:
        icon: 'android'
        user_font_size: '50sp'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        theme_text_color: 'Custom'
        text_color: 0,0,1,1
        on_release: app.username_checker()

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
    def username_checker(self):
        username_check_false = True
        username_text_data = self.scr.get_screen('by').ids.username_text.text
        print(username_text_data)
        try:
            int(username_text_data)
        except:
            username_check_false = False
        if username_check_false or username_text_data.split()==[]:
            cancel_btn = MDFlatButton(text='retry',on_release= self.close_dialog)
            self.username_dialog = MDDialog(title = 'Invalid Username',text = 'Plese ener a valid username',size_hint = (0.5,0.2), buttons = [cancel_btn])
            self.username_dialog.open()
        
    def close_dialog(self,obj):
        self.username_dialog.dismiss()
        

        
Demo().run()