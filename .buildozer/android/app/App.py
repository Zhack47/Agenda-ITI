from main import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
# from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
import main
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.lang import Builder
import User_keep_connection as Ukc


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
        self.clear_widgets()
        array_of_users = Ukc.load_usernames('user.csv')
        for i in range(len(array_of_users)):
            button_personal = Button(text=array_of_users[i]['first_name']+" "+array_of_users[i]['last_name'], font_size=34)
            button_personal.on_press = self.in_callback
            self.add_widget(button_personal)
        validation_button = Button(text='Valider', font_size=34)
        validation_button.on_press = self.callback_for_button
        validation_button.background_normal = ''
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

    def in_callback(self):
        self.clear_widgets()
        one =Ukc.load_usernames('user.csv')[0]
        self.res = main.main_mobile(one['first_name'], one['last_name'])
        if self.res == sr.__ERROR_NETWORK_UNREACHABLE__:
            return 0
        else:
            self.clear_widgets()
            result = EdtDisplay(color=[0.32, 1, 0.89, 1])
            result.halign = 'center'
            result.valign = "middle"
            result.text = self.res
            result.valign = "middle"
            result.halign = 'center'
            self.add_widget(result)
            return_button = Button(text='Retourner à l\'identification', font_size=24)
            return_button.on_press = self.callback_for_button_2
            return_button.background_normal = ''
            return_button.background_color = [0, 200, 0, 0]
            self.add_widget(return_button)
            self.do_layout()


    def callback_for_button(self):
        self.clear_widgets()
        self.res = main.main_mobile(self.nom.text, self.prenom.text)
        if self.res == sr.__ERROR_NETWORK_UNREACHABLE__:
            return 0
        else:
            Ukc.save_user('user.csv', self.prenom.text, self.nom.text)
            self.clear_widgets()
            # result = ScrollableLabel()  # (), halign='center', color=[0.32, 1, 0.89, 1])
            result = EdtDisplay(color=[0.32, 1, 0.89, 1])
            result.halign = 'center'
            result.valign = "middle"
            result.text = self.res
            result.valign = "middle"
            result.halign = 'center'
            self.add_widget(result)
            return_button = Button(text='Retourner à l\'identification', font_size=24)
            return_button.on_press = self.callback_for_button_2
            return_button.background_normal = ''
            return_button.background_color = [0, 200, 0, 0]
            self.add_widget(return_button)
            self.do_layout()

    def callback_for_button_2(self):
        self.clear_widgets()
        self.__init__()
