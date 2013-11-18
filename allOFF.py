#!/usr/bin/env python

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
LIGHT = 14
AIR = 15
VALVE = 18
GPIO.setup(LIGHT, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(AIR, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(VALVE, GPIO.OUT, initial=GPIO.HIGH)

GPIO.output(LIGHT, GPIO.HIGH)
GPIO.output(AIR, GPIO.HIGH)
GPIO.output(VALVE, GPIO.HIGH)
