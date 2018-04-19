#!/usr/bin/env python

"""
weather.py: read daily weather forecast from url
"""
__author__      = "Jason Sebek"
__copyright__   = "2018/04/19"

import urllib
from datetime import date
import requests

class Forecast(object):
    def __init__(self,hightemp,lowtemp,windyhours,rainyhours):
        # hightemp, lowtemp : integers
        #windyhours,rainyhours : dictionaries
        self.hightemp = hightemp
        self.lowtemp = lowtemp
        self.windyhours = windyhours
        self.rainyhours = rainyhours

googleweather = "https://www.google.co.jp/search?q=weather&rlz=1C1EJFA_enJP779JP779&oq=weather&aqs=chrome..69i57j69i61j69i60j69i61j35i39j0.1397j0j7&sourceid=chrome&ie=UTF-8"
f = urllib.urlopen(googleweather)
myfile = f.ride()
print(myfile)

g = requests.get(googleweather)
print g.text
