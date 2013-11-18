#!/usr/bin/env python

import RPi.GPIO as GPIO, time, logging, sys, signal, ConfigParser, os
import waterON

dir = os.path.dirname(os.path.abspath(__file__))
logfile = dir + '/logs/info.log'
logging.basicConfig(filename=logfile, level=logging.INFO)

Config = ConfigParser.ConfigParser()
Config.read(dir + '/config.ini')
duration = Config.getint('params','oxygen')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
AIR = 15
GPIO.setup(AIR, GPIO.OUT, initial=GPIO.HIGH)

def signal_handler(signal, frame):
	msg = 'You pressed Ctrl+C! Oxygenation STOPPED'
	logging.info(time.asctime(time.localtime()) + ' ' + msg)
        print msg
        waterON.stop()
	stop()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def start():
	#starting the air for oxygenation
	GPIO.output(AIR, GPIO.LOW)
	start = time.time()
	msg = 'Oxygenation STARTED'
	logging.info(time.asctime(time.localtime(start)) + ' ' + msg)
	print msg

	#checking how much time has elapsed for oxygenation
	#if time elapsed is more than 30 minues break
	elapsed = 0
	while True:
		elapsed = (time.time() - start)
		if elapsed > duration:
			break;
		time.sleep(1)

	#shutting the air down to avoid bubbles
	#in the watering system      
	GPIO.output(AIR, GPIO.HIGH)
	msg = 'Oxygenation stopped after %d seconds' % elapsed
	logging.info(time.asctime(time.localtime(start)) + ' ' + msg)
	print msg

	time.sleep(3)

	waterON.start()

def stop():
	GPIO.output(AIR, GPIO.HIGH)

if __name__ == "__main__":
        start()
