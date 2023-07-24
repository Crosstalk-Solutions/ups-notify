# This program runs as a daemon and periodically checks the status of the UPS with GPIO digital inputs
import RPi.GPIO as GPIO
import time
import os
import sys


# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)
# Choose a GPIO pin to use to read the UPS status
LO_DT_PIN = 17
# When the LO_DT pin is high, the UPS battery voltage is low
# Set the chosen pin to be an input pin and enable the internal pull-up resistor
GPIO.setup(LO_DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def low_battery():
    print('battery is low')
    # send a message to the user
    os.system('echo "UPS battery is low. Shutting down the system in 30 seconds." | wall')
    time.sleep(30)
    # shut down the system
    os.system('sudo shutdown -h now')


while True:
    if GPIO.input(LO_DT_PIN) == GPIO.HIGH:
        low_battery()
    time.sleep(10)