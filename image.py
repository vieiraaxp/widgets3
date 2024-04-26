from kivy.app import App 
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        return Image(source='/Users/aluno.sesipaulista/Downloads/vieiraa.jpeg')

if __name__ == '__main__':
    MyApp().run()