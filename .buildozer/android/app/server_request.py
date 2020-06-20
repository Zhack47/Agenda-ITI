import requests
from bs4 import BeautifulSoup
import time
import date_checker
import toast
__ERROR_NETWORK_UNREACHABLE__ = '1'


def recuperate():
    curr_date = date_checker.get_date_string()
    payload = {'cal': '2019-ASI-S6', 'getdate': curr_date}
    try:
        r = requests.get('http://193.49.10.198/day.php', params=payload)
        print(r.url)
    except:
        toast.toast('Network unreachable')
        return __ERROR_NETWORK_UNREACHABLE__
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.text)
    mydivs = soup.findAll("a", {"class": "ps"})
    courses = [i.attrs for i in mydivs]
    print(courses)
    for i in range(len(courses)):
        courses[i] = courses[i]['title'].split("\n")
    return courses