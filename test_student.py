import main
def test_set_get():
    students = main.set_students_data()
    for i in students:
        name = 'foo', str(i)
        i.set_prenom(name)
        i.set_nom(name)
        i.set_uml(name)
        i.set_progav(name)
        i.set_auto(name)
        i.set_stat(name)
        i.set_aps(name)
        assert(i.get_prenom() == name)
        assert(i.get_uml() == name)
        assert(i.get_progav() == name)
        assert(i.get_auto() == name)
        assert(i.get_stat() == name)
        assert(i.get_aps() == name)