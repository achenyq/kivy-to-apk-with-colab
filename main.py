from kivymd.app import MDApp
from kivy.app import App
from kivy.lang.builder import Builder 
import requests
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.screenmanager import ScreenManager
from kivy.properties import NumericProperty
from kivymd.uix.floatlayout import MDFloatLayout

#window size per pixels
#Window.size = (480,800) 

from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen

"""class ChokeScreen(MDScreen):
    pass

class MainScreen(MDScreen):
    # Your existing functions for signup, signin, setting, and Choke_performance
    pass

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ChokeScreen(name='choke'))
        return sm

    def go_back(self):
        self.root.current = 'main'

    def do_something(self):
        # Replace this function with the actual function for "Choke performance"
        print("Doing something on Choke performance screen!")

    # Your existing functions for signup, signin, setting, and Choke_performance

if __name__ == "__main__":
    MyApp().run()
"""
class HomePage(Screen):
    pass

class ChokeScreen(Screen):
    """method_coefficients = {
        "Gilbert": (0.1, 0.546, 1.89),
        "Ros": (0.05747, 0.5, 2),
        "Baxendall": (0.1046, 0.546, 1.93),
        "slb": (315, 0.56, 1.79),
        "Achong": (0.26178, 0.65, 1.88),
        "Pilevari": (0.02143, 0.313, 2.11)
    }

    def on_spinner_text(self, spinner, text):
        if text in self.method_coefficients:
            a, b, c = self.method_coefficients[text]
            self.ids.Emperial_Coefficient1.text = str(a)
            self.ids.Emperial_Coefficient2.text = str(b)
            self.ids.Emperial_Coefficient3.text = str(c)"""

    def calculate_flow_rate(self):
        try:
            P = float(self.ids.Upstream_pressure.text)
            GOR = float(self.ids.Producing_GOR.text)
            d = float(self.ids.Choke_Diameter.text)
            a = float(self.ids.Emperial_Coefficient1.text)
            b = float(self.ids.Emperial_Coefficient2.text)
            c = float(self.ids.Emperial_Coefficient3.text)

            q = a * P * (GOR ** -b) * (d ** c)
            #print(f"q = {a} * {P} * ({GOR} ** {-b}) * ({d} ** {c})")
            self.ids.result_label.text = f"Flow Rate: {q}"
        except ValueError as e:
            error_message = str(e)
            if "Upstream_pressure" in error_message:
                self.ids.result_label.text = "Invalid Upstream Pressure"
            elif "Producing_GOR" in error_message:
                self.ids.result_label.text = "Invalid Producing GOR"
            elif "Choke_Diameter" in error_message:
                self.ids.result_label.text = "Invalid Choke Diameter"
            elif "Emperial_Coefficient1" in error_message:
                self.ids.result_label.text = "Invalid Emperial Coefficient 1"
            elif "Emperial_Coefficient2" in error_message:
                self.ids.result_label.text = "Invalid Emperial Coefficient 2"
            elif "Emperial_Coefficient3" in error_message:
                self.ids.result_label.text = "Invalid Emperial Coefficient 3"
            else:
                self.ids.result_label.text = "Invalid Input"

    """def calculation(self,value):
        if value=="Gilbert":
            a,b,c= 0.1,0.546,1.89
        elif value=="Ros":
            a,b,c=0.05747,0.5,2
        elif value=="Baxendall":
            a,b,c=0.1046,0.546,1.93
        elif value=="slb":
            a,b,c=315,0.56,1.79
        elif value=="Achong":
            a,b,c=0.26178,0.65,1.88
        elif value=="Pilevari":
            a,b,c=0.02143,0.313,2.11
        self.ids.Emperial_Coefficient1.text = str(a)
        self.ids.Emperial_Coefficient2.text = str(b)
        self.ids.Emperial_Coefficient3.text = str(c)
        
        style=
        Button:
                size_hint:.12,.07
                background_normal: "pic/back.png"
                background_color_down: 0.83,0.83,0.83,1 
                pos_hint: {"x":0.01 , "y":0.92}
                on_release: app.root.current = "Home"
        
        Button:
                text:"Sing Up"
                size_hint:.1,.08
                pos_hint: {"center_x": 0.8, "center_y": 0.95}
                bg_color: 0.83,0.83,0.83,1
                background_color_down: 0.83,0.83,0.83,1
                font_size: "15sp"
                font_name: "Roboto-Medium.ttf"
                #on_release: app.signup()
            Button:
                text:"Sing In"
                size_hint:.1,.08
                pos_hint: {"center_x": 0.9, "center_y": 0.95}
                bg_color: 0.83,0.83,0.83,1
                background_color_down: 0.83,0.83,0.83,1
                font_size: "15sp"
                font_name: "Roboto-Medium.ttf"
                #on_release: app.signin()
            MDIconButton:
                icon: "cog-outline"  # Specify the icon name for the settings button
                pos_hint: {"x": 0.01, "y": 0.93}
                #on_release: app.setting()
                #on_release: app.setting()
        """
    def spinner_clicked(self,value):
        self.ids.click_label.text= f'You Selected {value} :'
        if value=="Gilbert":
            a,b,c= 0.1,0.546,1.89
        elif value=="Ros":
            a,b,c=0.05747,0.5,2
        elif value=="Baxendall":
            a,b,c=0.1046,0.546,1.93
        elif value=="slb":
            a,b,c=315,0.56,1.79
        elif value=="Achong":
            a,b,c=0.26178,0.65,1.88
        elif value=="Pilevari":
            a,b,c=0.02143,0.313,2.11
        self.ids.Emperial_Coefficient1.text = str(a)
        self.ids.Emperial_Coefficient2.text = str(b)
        self.ids.Emperial_Coefficient3.text = str(c)
    


class Manager(ScreenManager):
    pass

class NavBar(MDFloatLayout):
    pass

class FileScreen(Screen):
    pass

class SettingScreen(Screen):
    pass
class ChokePerformance(Screen):
    btn_choke = ObjectProperty(None)
    
    
class design(MDApp):
    def build(self):
        self.title='ProMate'
        self.icon = 'pic/PROMATE Logo(1).png'
        """self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"""
        
        style = Builder.load_file('main.kv')
        return style 
if __name__ == "__main__":
       
    design().run()
        