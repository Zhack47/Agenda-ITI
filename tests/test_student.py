import pytest as pt
import Student
import main
def test_set_get():
    students = main.set_students_data()
    for i in students:
        name = 'foo', str(i)
        i.set_prenom(name)
        assert(i.get_prenom() == name)