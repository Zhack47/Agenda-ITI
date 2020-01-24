import requests
from bs4 import BeautifulSoup
import time
import date_checker


def recuperate():
    # ip = 193.49.10.198
    time_str = date_checker.get_date_from_time_unit(time.ctime())
    curr_date = ''.join([time_str[2], time_str[1], time_str[0]])
    payload = {'cal' : '2019-ASI-S6', 'getdate' : curr_date}
    r = requests.get('http://193.49.10.198/day.php', params=payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.findAll("a", {"class": "ps"})
    courses = [(i.attrs) for i in mydivs]
    for i in range(len(courses)):
        courses[i] = courses[i]['title'].split("\n")
    return courses