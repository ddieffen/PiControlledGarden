PiControlledGarden
==================

RaspberryPi controlled garden for indoors herbs growing

Hardware Setup
==============

The installation, and setup of the PI are described on this webpage. Please refer to it in order to build the system
http://ddieffen.blogspot.com/2013/11/pi-controlled-garden.html

Running the scripts
===================

- Place all these scripts in the same folder
- Create a folder named logs >mkdir logs
- Edit the crontab jobs >sudo crontab -e

0 6 * * * /home/pi/scripts/lightSTART.py 2>>/home/pi/scripts/logs/cron.log
0 11 * * * /home/pi/scripts/airWaterSTART.py 2>>/home/pi/scripts/logs/cron.log

Let the system run.
