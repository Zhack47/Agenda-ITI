import Course


def test_set_get():
    course = Course.Course()
    name = 'foo', str(course)
    course.set_scheduled(name)
    course.set_title(name)
    course.set_teacher(name)
    course.set_group(name)
    course.set_is_lv(name)
    course.set_room(name)
    course.set_subject(name)
    assert(course.get_scheduled() == name)
    assert(course.get_group() == name)
    assert(course.get_is_lv() == name)
    assert(course.get_room() == name)
    assert(course.get_teacher() == name)
    assert(course.get_title() == name)