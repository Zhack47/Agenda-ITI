import Groups
import Course
import server_request as sr
import Student
from App import *
from kivy.app import App
# import User_keep_connection as Ukc

def set_students_data():
    dictionnary = Groups.extract_student_dicts('groupsASI32.csv')
    students = [None] * 69
    for i in range(len(students)):
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
    if courses_of_today == sr.__ERROR_NETWORK_UNREACHABLE__:
        return sr.__ERROR_NETWORK_UNREACHABLE__
    else:
        list_of_Courses =[None]*len(courses_of_today)
        for i in range(len(courses_of_today)):
            test_course = Course.Course()
            try:
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
                if (test_course.group == student.get_subject_group(subject)) or \
                        (test_course.group == student.get_subject_group(subject)[0]) or \
                        test_course.group == student.get_subject_group(subject_lv) or \
                        test_course.group == student.get_subject_group(subject_lv)[0]:
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
        if not (cl is None):
            print(cl.title)
            print(cl.teacher)
            print(cl.scheduled)
            print(cl.room)
            print()


def main_mobile(nom, prenom):
    students = set_students_data()
    id = retrieve_id_from_name(students, nom, prenom)
    classes = today_courses(students[id-1])
    if classes == sr.__ERROR_NETWORK_UNREACHABLE__:
        return  sr.__ERROR_NETWORK_UNREACHABLE__
    else:
        res = ''
        for cl in classes:
            if not (cl is None):
                res += cl.title
                res += '\n'
                res += cl.teacher
                res += '\n'
                res += cl.scheduled
                res += '\n'
                res += cl.room
                res += '\n'
                res += '\n'
        print('Done')
        return res

class MainApp(App):

    def build(self):
        log = LoginScreen()
        return log


if __name__ == '__main__':
    app = MainApp()
    app.run()


