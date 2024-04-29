from kivy.app import App
from kivy.uix.image import Imagem, AsyncImage
class MyApp(App):
    def build(self):
        return AsyncImage(source='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/de0d752c-92ee-4d13-a9d7-5f3c8f1ed9e7/d4fmr5i-97f3f76a-6334-4da2-a8c5-72ed37ac5796.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2RlMGQ3NTJjLTkyZWUtNGQxMy1hOWQ3LTVmM2M4ZjFlZDllN1wvZDRmbXI1aS05N2YzZjc2YS02MzM0LTRkYTItYThjNS03MmVkMzdhYzU3OTYucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.o9Ll62Vm5GpCXax00_DLIreozJwmDQy6TQDYxR78oOQ')
if __name__ == '__main__':
    MyApp().run()