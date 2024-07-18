#! /usr/bin/env python3

# -*- coding: utf-8 -*-

''' Display a digital clock with weather

Display a digital clock with weather conditions
'''

__author__ = 'Christopher R. Merlo'
__version__ = 0.1

import json
import os.path
import time
import tkinter as tk
import wget

from os import path
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

home = os.path.expanduser('~')

# Colors
metsblue = "#002d72"
metsorange = "#ff5910"

# Make the window
root = Tk()
root.configure(background = metsblue)

root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event:root.destroy())

img = ImageTk.PhotoImage(Image.open(home + '/python-clock/owm-icons/weather.png'))

def showtime():

    weather_string = 'Error Reading Weather'
    try:
        with open(home + '/python-clock/weather.txt', 'r') as weather_file:
            weather_string = weather_file.read()
    except:
        pass

    
    # Time stuff
    now = time.localtime()

    the_time = time.strftime("%-I:%M %p", now).lower()
    the_day = time.strftime("a", now)
    the_date = time.strftime("%a %b %-d", now)

    time_lbl.config(text = the_time)
    date_lbl.config(text = the_date)
    time_lbl.after(1000, showtime)

    img = ImageTk.PhotoImage(Image.open(home + '/python-clock/owm-icons/weather.png'))

    weather_lbl.config(text = weather_string)


# img = ImageTk.PhotoImage(Image.open(local_icon))

time_frame = Frame(root)
time_lbl = Label(time_frame, font = ("Audiowide", 100, "bold"),
                 background = metsblue,
                 foreground = 'white')
time_lbl.pack()

date_frame = Frame(root)
date_lbl = Label(date_frame, font = ("Rubik", 90, "bold"),
                 background = metsblue,
                 foreground = metsorange)
date_lbl.pack()

weather_frame = tk.Frame(root)
weather_frame.config(bg = metsblue)
img_lbl = Label(weather_frame, image = img, background = metsblue)
weather_lbl = Label(weather_frame, font = ("Audiowide", 40, "bold"),
                    background = metsblue,
                    foreground = 'white')
img_lbl.grid(row = 0, column = 0)
weather_lbl.grid(row = 0, column = 1)

time_frame.pack()
date_frame.pack()
weather_frame.pack()

showtime()

mainloop()

