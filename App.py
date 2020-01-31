from main import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.lang import Builder


Builder.load_string('''
<ScrollableLabel>:
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text

''')


class ScrollableLabel(ScrollView):
    text = StringProperty('')


class EdtDisplay(ScrollableLabel):
    def __init__(self, color, **kwargs):
        super(ScrollableLabel, self).__init__(**kwargs)
        self.text = ''
        self.color = color
    # def update_padding(self, text_input, *args):
    #     text_width = text_input._get_text_width(
    #         text_input.text,
    #         text_input.tab_width,
    #         text_input._label_cached
    #     )
    #     text_input.padding_x = (text_input.width - text_width) / 2

    def set_text(self, text):
        self.text = text


class LoginScreen(GridLayout):

    res = ''
    # edt = EdtDisplay()
    nom = TextInput
    prenom = TextInput
    def __init__(self, **kwargs):

        super(LoginScreen, self).__init__(**kwargs)
        validation_button = Button(text='Valider', font_size=34)
        validation_button.on_press = self.callback_for_button
        validation_button.background_normal = 'white.png'
        validation_button.background_color = [0, 1, 0, 0]
        self.cols = 1
        self.add_widget(Label(text='Nom'))
        self.nom = TextInput(multiline=False)
        self.add_widget(self.nom)
        self.add_widget(Label(text='Prénom'))
        self.prenom = TextInput(multiline=False)
        self.add_widget(self.prenom)
        # to_remove = Label(text='')
        self.add_widget(Label(text=''))
        self.add_widget(validation_button)
        # self.add_widget(self.edt)
        # self.edt = EdtDisplay()

    def callback_for_button(self):
        self.res = main_mobile(self.nom.text, self.prenom.text)
        # Ukc.save_user('user.csv', self.prenom, self.nom)
        self.clear_widgets()
        # result = ScrollableLabel()  # (), halign='center', color=[0.32, 1, 0.89, 1])
        result = EdtDisplay(color=[0.32, 1, 0.89, 1])
        result.halign = 'center'
        result.valign = "middle"
        result.text = self.res
        result.valign = "middle"
        result.halign = 'center'
        self.add_widget(result)
        self.do_layout()

    # def on_touch_up(self, touch):
    #     if touch.is_triple_tap:
    #         self.res = main_mobile(self.nom.text, self.prenom.text)
    #         self.clear_widgets()
    #         # result = ScrollableLabel()  # , halign ='center', color=[0.32, 1, 0.89, 1])
    #         result = edtDisplay()
    #         result.text = (self.res)
    #         self.add_widget(result)
    #         self.do_layout()
    #         self.do_layout()
    #         print(self.edt.text)
    #     else:
    #         pass


class MainApp(App):

    def build(self):
        log = LoginScreen()
        return log


if __name__ == '__main__':
    app = MainApp()
    app.run()
