#! /usr/bin/env python

from AdafruitFourCharAlphanumeric import FourCharDisplay
import time

myDisplay = FourCharDisplay(0x70)

myDisplay.write(" Go");

time.sleep(3)

while 1:

	myDisplay.set_register(myDisplay.FOUR_CHAR_REG_DISP_SET | 
			myDisplay.FOUR_CHAR_DISP_ON | 
			myDisplay.FOUR_CHAR_DISP_BLINK_OFF)

	myDisplay.write("TEST");

	time.sleep(2)

	myDisplay.write("1Hz");
	myDisplay.set_register(myDisplay.FOUR_CHAR_REG_DISP_SET | 
			myDisplay.FOUR_CHAR_DISP_ON | 
			myDisplay.FOUR_CHAR_DISP_BLINK_1HZ)

	time.sleep(5)

	myDisplay.write("2Hz");
	myDisplay.set_register(myDisplay.FOUR_CHAR_REG_DISP_SET | 
			myDisplay.FOUR_CHAR_DISP_ON | 
			myDisplay.FOUR_CHAR_DISP_BLINK_2HZ)

	time.sleep(5)