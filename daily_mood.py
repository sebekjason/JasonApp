#!/usr/bin/env python

"""
daily_mood.py: Construction of classes for daily wellbeing monitoring
"""
__author__      = "Jason Sebek"
__copyright__   = "2018/04/19"

from datetime import timedelta as delt
from datetime import date

class Status(Object):
    "an object to track daily status"
    scale = 10
    today = date.today()
    def __init__(self, wellnum, date, weather):
        self.wellnum = wellnum
        self.date = date



