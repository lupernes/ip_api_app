import requests
import json
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input_data = TextInput(hint_text="Введите ip", multiline=False)
        self.buttonin = Button(text="Send", on_press=self.api_ip_req)
        self.labres = Label(text="")
        
    def api_ip_req(self, *args):
        data = self.input_data.text
        res = requests.get(f'http://ip-api.com/json/{data}').text
        res_decode = json.loads(res)
        data = res_decode.get("status") +  "\n" + res_decode.get("country") + "\n" + res_decode.get('city') + "\n" + res_decode.get("as")       
        self.labres.text = data
        
    

        
    def build(self):
        data = self.input_data.text
        box = BoxLayout(orientation="vertical")
        box.add_widget(self.input_data)
        box.add_widget(self.buttonin)
        box.add_widget(self.labres)
        return box
    
if __name__ == "__main__":
    MyApp().run()