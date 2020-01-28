import Groups
import Course
import server_request as sr
import Student

from kivy.uix.widget import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.lang import Builder

long_text = 'yay moo cow foo bar moo baa ' * 100

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



Nom = ''
Prenom = ''

dictionnary = Groups.extract_student_dicts('groupsASI32.csv')
students = [None]*69



def set_students_data():
    print('access')
    for i in range(len(students)):
        print(i)
        students[i] = Student.Student()
    for i in range(len(students)):
        students[i].id = i+1
        students[i].set_auto(dictionnary[i]['AUTO\n4,5'])
        students[i].set_ang(dictionnary[i]['ANG\n1,5'])
        students[i].set_aps(dictionnary[i]['APS\n1,5'])
        students[i].set_capteur(dictionnary[i]['CAPT\n4,5'])
        students[i].set_compil(dictionnary[i]['COMPIL\n1'])
        students[i].set_droit(dictionnary[i]['DROIT\n1,5'])
        students[i].set_prenom(dictionnary[i]['Prénoms'])
        students[i].set_nom(dictionnary[i]['Noms'][:-1])
        students[i].set_qua(dictionnary[i]['QUALITE\n1,5'])
        students[i].set_progav(dictionnary[i]['PROGAV\n4,5'])
        students[i].set_tsa(dictionnary[i]['TSA\n2,5'])
        students[i].set_tw(dictionnary[i]['TW I\n2,5'])
        students[i].set_tuteur(dictionnary[i]['Tuteur'])
        students[i].set_stat(dictionnary[i]['STAT\n4,5'])
        students[i].set_lv2(dictionnary[i]['LV2\n1,5'])
    return students

def today_courses(student):
    courses_of_today = sr.recuperate()
    print(len(courses_of_today))
    print(courses_of_today)
    list_of_Courses =[None]*len(courses_of_today)
    for i in range(len(courses_of_today)):
        test_course = Course.Course()
        try :
            test_course.set_scheduled(courses_of_today[i][3])
        except IndexError:
            test_course.set_scheduled('N/A')
        try:
            test_course.set_room(courses_of_today[i][2])
        except IndexError:
            test_course.set_room('N/A')
        try:
            test_course.set_teacher(courses_of_today[i][1])
        except IndexError:
            test_course.set_teacher('N/A')
        test_course.set_title(courses_of_today[i][0])
        test_course.group = Groups.extract_group_from_course(test_course)
        test_course.subject = Course.extract_subject_from_course_title(test_course.title)
        try:
            subject = test_course.title.split(':')[1].split('-')[1].split(' ')[0]
            subject_lv =test_course.title.split(' ')[2]
        except IndexError:
            subject = subject_lv = 'N/A'
        if test_course.group != '*':
            if (test_course.group) == (student.get_subject_group(subject)) or (test_course.group) == student.get_subject_group(subject)[0] or test_course.group == student.get_subject_group(subject_lv) or test_course.group == student.get_subject_group(subject_lv)[0]:
                list_of_Courses[i] = test_course
        else:
            list_of_Courses[i] = test_course
    return list_of_Courses


def retrieve_id_from_name(students, nom, prenom):
    for s in students:
        if (s.Nom == nom) and (s.Prenom == prenom):
            return s.id
    return -1

def main():
    nom = input("Nom :")
    prenom = input('Prénom :')
    students = set_students_data()
    id = retrieve_id_from_name(students, nom, prenom)
    classes = today_courses(students[id-1])
    for cl in classes:
        if cl != None:
            print(cl.title)
            print(cl.teacher)
            print(cl.scheduled)
            print(cl.room)
            print()



def main_mobile(nom, prenom):
    students = set_students_data()
    id = retrieve_id_from_name(students, nom, prenom)
    classes = today_courses(students[id-1])
    res =''
    for cl in classes:
        if cl != None:
            res+=cl.title
            res+='\n'
            res+=cl.scheduled
            res+='\n'
            res+=cl.room
            res+='\n'
            res+='\n'
    print('Done')
    return res



class edtDisplay(ScrollableLabel):
    def __init__(self, **kwargs):
        super(ScrollableLabel, self).__init__(**kwargs)
        self.text = ''

    def update_padding(self, text_input, *args):
        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached
        )
        text_input.padding_x = (text_input.width - text_width) / 2

    def set_text(self, text):
        self.text = text




class LoginScreen(GridLayout):

    res = ''
    edt = edtDisplay()
    def __init__(self, **kwargs):

        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Nom'))
        self.nom = TextInput(multiline=False)
        self.add_widget(self.nom)
        self.add_widget(Label(text='Prénom'))
        self.prenom = TextInput(multiline=False)
        self.add_widget(self.prenom)
        to_remove = Label(text='')
        self.add_widget(Label(text='Cours de la journée'))
        # self.add_widget(self.edt)
        self.edt = edtDisplay()

    def on_touch_up(self, touch):
        if touch.is_triple_tap:
            self.res = main_mobile(self.nom.text, self.prenom.text)
            self.clear_widgets()
            # result = ScrollableLabel()  # , halign='center', color=[0.32, 1, 0.89, 1])
            result = edtDisplay()
            result.text = (self.res)
            self.add_widget(result)
            self.do_layout()
            self.do_layout()
            print(self.edt.text)
        else:
            pass




class MainApp(App):

    def build(self):
        log = LoginScreen()
        return log


if __name__ == '__main__':
    app = MainApp()
    app.run()