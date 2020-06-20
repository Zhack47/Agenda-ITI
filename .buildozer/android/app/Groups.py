import csv


def extract_student_dicts(csv_filename):
    students_dicts = [None]*71
    i = 0
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            students_dicts[i] = row
            i += 1
    return students_dicts


def extract_group_from_course(course):
    if 'Cm : ' in course.title:
        group = '*'
    elif 'pao' in course.title:
        group = 'pao'
    elif 'Asi32' in course.title:
        try:
            group = course.title.split('(')[-1].split(')')[0].split('_TD')[1]
        except IndexError:
            group = 'N/A'
    elif 'Anglais' in course.title:
        group = course.title.split('(')[-1].split(')')[0].split('_TD')[1]
    elif ('Espagnol' in course.title) and ('RN' in course.title):
        group = 'ESP RN'
    elif 'Espagnol' in course.title:
        group = 'ESP'
        # group = course.title.split('(')[1].split(')')[0].split('TD')[1]
    elif 'Allemand' in course.title:
        group = 'ALL'
        # group = course.title.split('(')[1].split(')')[0].split('_TD')[1]
    elif 'Fle' in course.title:
        group = 'Fle'
        # group = course.title.split('(')[1].split(')')[0].split('_TD')[1]
    else:
        group = '*'
    return group
