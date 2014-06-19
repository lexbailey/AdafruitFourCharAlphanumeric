#! /usr/bin/env python

from AdafruitFourCharAlphanumeric import FourCharDisplay
import time

myDisplay = FourCharDisplay(0x70)

myDisplay.write("....");

time.sleep(3)

while 1:

	myDisplay.set_register(myDisplay.FOUR_CHAR_REG_DISP_SET | 
			myDisplay.FOUR_CHAR_DISP_ON | 
			myDisplay.FOUR_CHAR_DISP_BLINK_OFF)

	myDisplay.write(chr(0)+chr(1)+chr(2)+chr(3));
	time.sleep(5)
	myDisplay.write(chr(4)+chr(5)+chr(6)+chr(7));
	time.sleep(5)
	myDisplay.write(chr(8)+chr(9)+chr(10)+chr(11));
	time.sleep(5)
	myDisplay.write(chr(12)+chr(13)+chr(14)+chr(15));
	time.sleep(5)