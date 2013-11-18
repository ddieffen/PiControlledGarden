#!/usr/bin/env python

import RPi.GPIO as GPIO, time, logging, sys, signal, ConfigParser, os

dir = os.path.dirname(os.path.abspath(__file__))
logfile = dir + '/logs/info.log'
logging.basicConfig(filename=logfile, level=logging.INFO)

Config = ConfigParser.ConfigParser()
Config.read(dir + '/config.ini')
duration = Config.getint('params','light')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LIGHT = 14
GPIO.setup(LIGHT, GPIO.OUT, initial=GPIO.HIGH)

def signal_handler(signal, frame):
	msg = 'You pressed Ctrl+C! Lighting STOPPED'
        logging.info(time.asctime(time.localtime()) + ' ' + msg)
        print msg
	GPIO.output(LIGHT, GPIO.HIGH)
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def start():
	#starting the light and saving the time at which it started
	start = time.time()
	GPIO.output(LIGHT, GPIO.LOW)
	msg = 'Light STARTED'
        logging.info(time.asctime(time.localtime(start)) + ' ' + msg)
        print msg

	#checking how much time has elapsed every hours
	#if time elapsed is more than 8 hours then break
	elapsed = 0
	while True:
		elapsed = (time.time() - start)
		if elapsed > duration:
			break;
		time.sleep(1)

	#shutting the light down after 8 hours
	GPIO.output(LIGHT, GPIO.HIGH)
	msg = 'Light STOPPED after %d seconds' % elapsed
        logging.info(time.asctime(time.localtime(start)) + ' ' + msg)
        print msg
	

if __name__ == "__main__":
        start()

