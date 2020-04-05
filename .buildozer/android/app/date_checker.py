#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import datetime


def check_if_date_is_valid(date):
    day, month, year = date[0], date[1], date[2]

    is_valid_date = True
    try:
        datetime(int(year), int(month), int(year))
    except ValueError:
        is_valid_date = False
    return is_valid_date


def get_month_number_from_time_unit(i):
    switcher = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
    return switcher.get(i, "Invalid Month")


def get_month_number_french(i):
    switcher = {
        "janvier": "01",
        "février": "02",
        "fars": "03",
        "avril": "04",
        "mai": "05",
        "juin": "06",
        "juillet": "07",
        "août": "08",
        "septembre": "09",
        "octobre": "10",
        "novembre": "11",
        "décembre": "12",
    }
    return switcher.get(i, "Invalid Month")


Days_of_the_week = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
Day_number = ["31", "30", "29", "28", "27", "26", "25", "24", "23", "22", "21", "20", "19", "18", "17", "16", "15", "14", "13", "12", "11", "10", "9",  "8",  "7",  "6",
              "5",  "4",  "3",  "2", "1"]
MonthsFr = ["janvier", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jul", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Years = [1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987,
         1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
         2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
         2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041,
         2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049]


def get_date_from_string(string):
    year, data = detect_str_year_number_in_str(string, Years)
    month, data = detect_str_month_number_in_str_fr(string, Months)
    day, data = detect_str_day_number_in_str(string, Day_number)
    return day, month, year


def get_date_from_time_unit(string):
    string = " ".join([string.split(" ")[0], string.split(" ")[1], string.split(" ")[3], string.split(" ")[-1]])
    print("time is {}".format(string))
    year, data = detect_str_year_number_in_str(string, Years)
    month, data = detect_str_month_number_in_str(data, Months)  # string.split(" ")[1], Months)
    day, data = detect_str_day_number_in_str(data, Day_number)  # string.split(" ")[2], Day_number)
    print(day, month, year)
    return [day, month, year]


def detect_str_month_number_in_str(data, months):
    for string in Months:
        data.replace(str(string), '')
        if str(string) in data:
            data = data.replace(str(string), '')
            return get_month_number_from_time_unit(string), data
    print('No Month found')
    return False, data

def detect_str_month_number_in_str_fr(data, months):
    for string in MonthsFr:
        if str(string) in data:
            data = data.replace(str(string), '')
        return get_month_number_french(string), data
    print('No Month found')
    return False, data


def detect_str_day_number_in_str(data, day_number):
    for string in day_number:
        if str(string) in data:
            data = data.replace(str(string), '')
            if len(str(string)) == 1:
                return"0"+string, data
            else:
                return str(string), data
    return False, data


def detect_str_year_number_in_str(data, years):
    for string in years:
        if str(string) in data:
            data = data.replace(str(string), '')
            return str(string), data
    print('No Year found')
    return False, data
