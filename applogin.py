from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.clock import Clock



class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [30, 50]
        self.spacing = 10
        self.background_color = get_color_from_hex('#0B1732')  

        self.logo = Image(source='https://upload.wikimedia.org/wikipedia/commons/9/93/Wordpress_Blue_logo.png')
        self.add_widget(self.logo)

        self.login_box = BoxLayout(orientation='horizontal', spacing=10)
        self.password_box = BoxLayout(orientation='horizontal', spacing=10)
        
        self.login_label = Label(text='Login:', size_hint_x=None, width=100)
        self.password_label = Label(text='Senha:', size_hint_x=None, width=100)
        
        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.check_login)

        self.error_label = Label(text='', color=(1, 0, 0, 1)) 
        self.forgot_password_button = Button(text="Esqueci minha senha")
        self.forgot_password_button.bind(on_press=self.send_recovery_email)

        self.signup_button = Button(text="Cadastro")
        self.signup_button.bind(on_press=self.open_signup_page)

        self.login_box.add_widget(self.login_label)
        self.login_box.add_widget(self.username_input)
        self.password_box.add_widget(self.password_label)
        self.password_box.add_widget(self.password_input)

        self.add_widget(self.login_box)
        self.add_widget(self.password_box)
        self.add_widget(self.login_button)
        self.add_widget(self.forgot_password_button)
        self.add_widget(self.signup_button)
        self.add_widget(self.error_label)

        self.default_username = "admin"
        self.default_password = "admin"

        self.login_button.color = get_color_from_hex('#00FF00')

    def check_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if username == self.default_username and password == self.default_password:
            self.error_label.text = "Login feito!"
        else:
            self.error_label.text = "Usuário ou senha inválidos!"

    def send_recovery_email(self, instance):
        self.error_label.text = "Um email de recuperação de senha foi enviado para o seu endereço."

    def open_signup_page(self, instance):
        self.clear_widgets()
        self.add_widget(SignUpScreen())


class SignUpScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(SignUpScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [30, 200]
        self.spacing = 10
        self.background_color = get_color_from_hex('#0B1732')

        self.login_box = BoxLayout(orientation='horizontal', spacing=10)
        self.password_box = BoxLayout(orientation='horizontal', spacing=10)
        
        self.login_label = Label(text='novo usuário:', size_hint_x=None, width=100)
        self.password_label = Label(text='nova senha:', size_hint_x=None, width=100)
        
        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.signup_button = Button(text='Sign Up')
        self.signup_button.bind(on_press=self.register_user)

        self.error_label = Label(text='', color=(1, 0, 0, 1)) 

        self.login_box.add_widget(self.login_label)
        self.login_box.add_widget(self.username_input)
        self.password_box.add_widget(self.password_label)
        self.password_box.add_widget(self.password_input)

        self.add_widget(self.login_box)
        self.add_widget(self.password_box)
        self.add_widget(self.signup_button)
        self.add_widget(self.error_label)

    def register_user(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        login_screen = App.get_running_app().root
        login_screen.default_username = username
        login_screen.default_password = password

        self.error_label.text = "Cadastro realizado com sucesso!"
 
        Clock.schedule_once(self.go_to_login_screen, 1)

    def go_to_login_screen(self, dt):
        login_screen = App.get_running_app().root
        login_screen.clear_widgets()
        login_screen.add_widget(LoginScreen())


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()