from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding= 200)
        botao1 = Button(text='.', background_color =(0.2, 0.7, 0.3, 1), font_size = 20)
        botao2 = Button(text='Clique aqui', halign ='center')
        botao3 = Button(text='Clique para continuar', background_color = (0.9, 0.5, 0.1, 1), font_size = 30)
        layout.add_widget(botao1)
        layout.add_widget(botao2)
        layout.add_widget(botao3)

        def acao_botao(instance):
            instance.text = 'email de recuperação de senha enviado.'
        
        botao4 = Button(text = 'botão 4')
        botao4.bind(on_press = acao_botao)
        layout.add_widget(botao4)
        info_label = Label(text = 'copywrite')
        layout.add_widget(info_label)
        return layout

if __name__ == '__main__':
    MyApp().run()
