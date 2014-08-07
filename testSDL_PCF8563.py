#!/usr/bin/env python
#
# Test SDL_PCF8563
# John C. Shovic, SwitchDoc Labs
# 08/07/2014
#
#

# imports

import sys
import time
import datetime

import SDL_PCF8563

# Main Program

print ""
print "Test SDL_PCF8563 Version 1.0 - SwitchDoc Labs"
print ""
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")

filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()

pcf8563 = SDL_PCF8563.SDL_PCF8563(1, 0x51)
pcf8563.write_now()

# Main Loop - sleeps 10 minutes, then reads and prints values of all clocks


while True:

	currenttime = datetime.datetime.utcnow()

	deltatime = currenttime - starttime
 
	print ""
	print "Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S")
	
	print "PCF8563=\t\t%s" % pcf8563.read_datetime()

	time.sleep(10.0)
