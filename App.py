from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import main
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Nom'))
        self.nom = TextInput(multiline=False)
        self.add_widget(self.nom)
        self.add_widget(Label(text='Prénom'))
        self.prenom = TextInput(multiline=False)
        self.add_widget(self.prenom)

    def on_touch_move(self, touch):
        main.main_mobile(self.nom.text, self.prenom.text)


class MainApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    app = MainApp()
    app.run()