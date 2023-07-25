# This program runs as a daemon and periodically checks the status of the UPS with GPIO digital inputs
import RPi.GPIO as GPIO
import time
import os


# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)
# Choose a GPIO pin to use to read the UPS status
LO_DT_PIN = 17
DISCORD_WEBHOOK_URL = 'REPLACE WITH YOUR DISCORD WEBHOOK URL'
DISCORD_USER_ID = '408878638109425665'
# When the LO_DT pin is high, the UPS battery voltage is low
GPIO.setup(LO_DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def low_battery():
    print('battery is low')
    # send a discord webhook
    os.system('curl -H "Content-Type: application/json" -X POST -d \'{"content": "<@' + DISCORD_USER_ID + '> UPS battery is low. Shutting down the system in 30 seconds."}\' ' + DISCORD_WEBHOOK_URL)
    # send a message to the user
    os.system('echo "UPS battery is low. Shutting down the system in 30 seconds." | wall')
    # time.sleep(30)
    # shut down the system
    # os.system('sudo shutdown -h now')
    # exit the script
    # exit()


while True:
    if GPIO.input(LO_DT_PIN) == GPIO.HIGH:
        low_battery()
    time.sleep(10)