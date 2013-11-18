#!/usr/bin/env python

import RPi.GPIO as GPIO, time, logging, sys, signal, ConfigParser, os

dir = os.path.dirname(os.path.abspath(__file__))
logfile = dir + '/logs/info.log'
logging.basicConfig(filename=logfile, level=logging.INFO)

Config = ConfigParser.ConfigParser()
Config.read(dir + '/config.ini')
duration = Config.getint('params','water')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
VALVE = 18
GPIO.setup(VALVE, GPIO.OUT, initial=GPIO.HIGH)

def signal_handler(signal, frame):
        msg = 'You pressed Ctrl+C! Watering STOPPED'
	logging.info(time.asctime(time.localtime()) + ' ' + msg)
	print msg
	stop()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def start():
	#start watering the plants
	GPIO.output(VALVE, GPIO.LOW)
	start = time.time()
	msg = 'Watering STARTED'
	logging.info(time.asctime(time.localtime(start)) + ' ' + msg)
	print msg

	time.sleep(duration)

	elapsed = (time.time() - start)
	GPIO.output(VALVE, GPIO.HIGH)
	msg = 'Watering STOPPED after %d seconds' % elapsed
	logging.info(time.asctime(time.localtime(start)) + ' ' + msg)
	print msg

def stop():
	GPIO.output(VALVE, GPIO.HIGH)

if __name__ == "__main__":
	start()
