# python-clock

This program makes a nice digital clock with weather data appear on your Raspberry Pi's monitor.  I wrote this in particular to use with the Raspberry Pi 7" Touch Display (https://www.raspberrypi.com/products/raspberry-pi-touch-display/).

## Screenshot
![Clock screenshot](https://chrismerlo.net/clock.png "Clock screenshot")

## Code Components

### `clock.py`
This is the main script, which makes the clock appear and run.

### `weather.py`
This reads the weather data that was downloaded by the cronfile and formats the weather info for display.  It will download the current weather's icon if necessary, and symlink the file weather.png to the current conditions' icon.

### `cronfile`
Calls Open Weather Map's API every five minutes and downloads data into a JSON file read by `weather.py`.  Then, one minute later, runs `weather.py` so that the display can be updated.  (See https://openweathermap.org/api/one-call-3#current)

### `clock.desktop`
A file that runs when XDG starts up -- as long as you've copied it into `/etc/xdg/autostart` -- which will make the clock start up upon reboot

## Other Needs

* I made the default user on this pi have the username `clock`.  There are a couple of things to change if you keep the default username `pi` or use some other username.

### Fonts
This code uses:
* Audiowide (https://fonts.google.com/specimen/Audiowide?query=audiowide) for the time and weather
* Rubik for the date