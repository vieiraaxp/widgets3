from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Email"))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)
        self.add_widget(Label(text="Password"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)
        self.login_button = Button(text="Sign In", on_press=self.login)
        self.add_widget(self.login_button)

    def login(self, instance):
        email = self.email.text
        password = self.password.text

        print(f"Email: {email}, Password: {password}")

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    LoginApp().run()