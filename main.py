from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
import requests

class JustLetsApp(App):
    def build(self):
        # Dark theme color scheme
        Window.clearcolor = (0.07, 0.07, 0.07, 1)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title = Label(text="Just Lets App", font_size='24sp', bold=True, size_hint_y=None, height=50)
        layout.add_widget(title)
        
        # Razorpay Button
        pay_btn = Button(text="Pay ₹500 with Razorpay", background_color=(0, 0.5, 0, 1), font_size='18sp', bold=True, size_hint_y=None, height=60)
        layout.add_widget(pay_btn)
        
        # Ask AI Label
        ai_label = Label(text="Welcome! Ask AI anything below:", font_size='16sp', size_hint_y=None, height=40, halign='left')
        layout.add_widget(ai_label)
        
        # Chat Display Area
        self.chat_area = Label(text="", font_size='14sp', size_hint_y=1, valign='top', halign='left')
        self.chat_area.bind(size=self.chat_area.setter('text_size'))
        layout.add_widget(self.chat_area)
        
        # Input row
        input_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        self.user_input = TextInput(multiline=False, background_color=(0.17, 0.17, 0.17, 1), foreground_color=(1, 1, 1, 1), font_size='16sp')
        send_btn = Button(text="Send", background_color=(0, 0.48, 0.8, 1), font_size='16sp', size_hint_x=None, width=100)
        
        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        layout.add_widget(input_layout)
        
        return layout

if __name__ == '__main__':
    JustLetsApp().run()