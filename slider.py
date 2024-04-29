from kivy.app import App
from kivy.uix.slider import Slider

class MyApp(App):
    def build(self):
        return Slider(min=80, max=500, value=100)
if __name__ == '__main__':
    MyApp().run()