#!/usr/bin/python

import sys

try:
	arg = str(sys.argv[1])
	for line in reversed(list(open(arg))):
    		print(line.rstrip())
	pass

except IndexError:
	print "Error: No File Given!"
	sys.exit()

except IOError as (errno, strerror):
    if errno == 13:
    	print "Error 2: Permission Denied!"

    if errno == 2:
    	print "Error 1: Doesen't Exist!"

    if errno == 21:
    	print "Error 4: Not a File!"
