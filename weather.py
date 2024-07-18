#! /usr/bin/env python3

# -*- coding: utf-8 -*-

'''Read weather data

This script uses weather data downlaoded previously for use
in the python clock program.
'''

__author__ = 'Christopher R. Merlo'
__version__ = 0.1

import json
import os.path
import wget

from datetime import datetime
from os import path

home = os.path.expanduser('~')

now = datetime.now()

degree_sign= u'\N{DEGREE SIGN}'

log_file = open(home + '/python-clock/weather.log', 'a')

icon_dir = home + '/python-clock/owm-icons/'

weather_string = ''

try:
    with open(home + '/python-clock/weather.json', 'r') as file:
        data = json.load(file)

        icon = data['weather'][0]['icon']
        filename = icon + "@2x.png"
        url = "http://openweathermap.org/img/wn/" + filename

        ###

        temp = round(data['main']['temp'])
        condition = data['weather'][0]['description']
        feel = round(data['main']['feels_like'])

        # weather_string = '%i%s (%i)%s %s\n' % ( temp, degree_sign, feel, degree_sign, condition.title())
        weather_string = '%i%s (Feels like %i%s)\n%s\n' % (temp, degree_sign, feel, degree_sign, condition)

        with open(home + '/python-clock/weather.txt', 'w') as wfile:
            wfile.write(weather_string)
        wfile.close()

    if not path.exists(icon_dir + filename):
        wget.download(url, icon_dir + filename)

    if path.exists(icon_dir + 'weather.png'):
        os.unlink(icon_dir + 'weather.png')
        
    os.symlink(icon_dir + filename, icon_dir + 'weather.png')


except Exception as e:
    log_file.write(str(now) + ': ' + str(e) + '\n')

finally:
    log_file.close()
