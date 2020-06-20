#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import date


def get_date_string():
    return "".join(str(date.today()).split("-"))
