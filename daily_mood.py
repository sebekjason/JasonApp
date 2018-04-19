#!/usr/bin/env python

"""
daily_mood.py: Construction of classes for daily wellbeing monitoring
"""
__author__      = "Jason Sebek"
__copyright__   = "2018/04/19"

from datetime import timedelta as delt
from datetime import date

class Status(object):
    "an object to track daily status"
    scale = 10
    today = date.today()
    def __init__(self, wellnum, weather):
        self.wellnum = wellnum
        self.date = date
    def getwellnum(self):
        return self.wellnum
    def readout(self):
        print self.getwellnum(), '/', self.scale
        print str(self.today)
        print weather


weather = []
today = Status(8,weather)
today.readout()
