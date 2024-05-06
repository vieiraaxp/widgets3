from kivy.app import App 
from kivy.uix.video import Video

class MyApp(App):
    def build(self):
        return Video(source='')

if __name__ == '__main__':
    MyApp().run()