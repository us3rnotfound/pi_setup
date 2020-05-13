# pi_setup
Setup files for Raspberry Pi to accommodate power button and fan mod.

1. Place rc.local in /etc/rc.local, make sure it is executable.
2. Place fan_turn_on.py in /usr/local/bin/.
3. Grab last lines of config.txt to get the settings for power button, edit /boot/config.txt to match.
