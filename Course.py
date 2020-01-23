class Course:
    title = ''
    teacher = ''
    group = ''
    room = ''
    subject = ''
    scheduled = ''
    is_lv = False

    def __init__(self):
        pass

    def set_teacher(self, teacher):
        self.teacher = teacher

    def set_title(self, title):
        self.title = title

    def set_group(self, group):
        self.group = group

    def set_room(self, room):
        self.room = room

    def set_subject(self, subject):
        self.subject = subject

    def set_scheduled(self, scheduled):
        self.scheduled = scheduled

    def set_is_lv(self, is_lv):
        self.is_lv = is_lv


def extract_subject_from_course_title(string):
    if 'pao' in string:
        subject = 'pao'
    elif 'Anglais' in string:
        subject = 'Anglais'
    elif ('Espagnol' in string) and ('RN' in string):
        subject = 'Espagnol (remise à niveau)'
    elif 'Espagnol' in string:
        subject = 'Espagnol'
    elif 'Allemand' in string:
        subject = 'Allemand'
    else:
        subject =string.split(':')[1].split(' ')[1]
    return subject