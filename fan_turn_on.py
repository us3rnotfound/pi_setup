#!/usr/bin/env python

#import subprocess
import RPi.GPIO as GPIO

# Setup GPIO to refer to pin numbers:
GPIO.setmode(GPIO.BOARD)

# Setup pin 5 as an input with internal pull-up since 
# bringing it to GND is what activates shutdown.
#GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup Pin 11 as fan output.
GPIO.setup(11, GPIO.OUT)

# Turn on FAN
GPIO.output(11, True)

# Blocking function call:
# When user presses power button, this 
# connects Pin 5 to Ground, hence it is a falling edge.
# Also includes 20 ms of debouncing.
#GPIO.wait_for_edge(5, GPIO.FALLING, bouncetime=20)

# Turn fan OFF
#GPIO.setup(11, False)

# Cleanup GPIO:
#GPIO.cleanup()

# Shutdown.
#subprocess.call('sudo shutdown -h now', shell=True)
