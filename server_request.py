import requests
from bs4 import BeautifulSoup
import time
import date_checker


def recuperate():
    time_str = date_checker.get_date_from_time_unit(time.ctime())
    curr_date = ''.join([time_str[2], time_str[1], time_str[0]])
    r = requests.get('http://agendas.insa-rouen.fr/day.php?cal=2019-ASI-S5&getdate=', curr_date)
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.findAll("a", {"class": "ps"})
    courses = [(i.attrs) for i in mydivs]
    for i in range(len(courses)):
        courses[i] = courses[i]['title'].split("\n")
    return courses
