class Student:
    id = 0
    Prenom = ''
    Nom = ''
    capt = ''
    auto = ''
    progav = ''
    uml = ''
    tw = ''
    compil = ''
    tsa = ''
    stat = ''
    lv2 = ''
    ang = ''
    aps = ''
    droit = ''
    qua = ''
    tuteur = ''

    def __init__(self):
        pass

    def set_prenom(self, prenom):
        self.Prenom = prenom

    def set_nom(self, nom):
        self.Nom = nom

    def set_capteur(self, capteur):
        self.capt = capteur

    def set_auto(self, auto):
        self.auto = auto

    def set_progav(self, progav):
        self.progav = progav

    def set_uml(self, uml):
        self.uml = uml

    def set_tw(self, tw):
        self.tw = tw

    def set_compil(self, compil):
        self.compil = compil

    def set_tsa(self, tsa):
        self.tsa = tsa

    def set_stat(self, stat):
        self.stat = stat

    def set_lv2(self, lv2):
        self.lv2 = lv2

    def set_ang(self, ang):
        self.ang = ang

    def set_aps(self, aps):
        self.aps = aps

    def set_droit(self, droit):
        self.droit = droit

    def set_qua(self, qua):
        self.qua = qua

    def set_tuteur(self, tuteur):
        self.tuteur = tuteur

    def get_prenom(self):
        return self.Prenom

    def get_nom(self):
        return self.Nom

    def get_capteur(self):
        return self.capt

    def get_auto(self):
        return self.auto

    def get_progav(self):
        return self.progav

    def get_uml(self):
        return  self.uml

    def get_tw(self):
        return self.tw

    def get_compil(self):
        return  self.compil

    def get_tsa(self):
        return self.tsa

    def get_stat(self):
        return  self.stat

    def get_lv2(self):
        return self.lv2

    def get_ang(self):
        return self.ang

    def get_aps(self):
        return self.aps

    def get_droit(self):
        return self.droit

    def get_qua(self):
        return  self.qua

    def get_tuteur(self):
        return self.tuteur

    def get_subject_group(self, course_title):
        if course_title == 'capt':
            return self.get_capteur() + ' '
        elif course_title == 'auto':
            return self.get_auto() + ' '
        elif course_title == 'stat':
            return self.get_stat() + ' '
        elif course_title == 'progav':
            return self.get_progav() + ' '
        elif course_title == 'umlp':
            return self.get_uml() + ' '
        elif course_title == 'qua':
            return self.get_qua() + ' '
        elif course_title == 'Anglais':
            return self.get_ang() + ''
        elif course_title == 'Espagnol' or course_title == 'Allemand' or course_title == 'Fle':
            return self.get_lv2() + ''
        else:
            return 'aa'

    def get_id(self):
        return self.id
