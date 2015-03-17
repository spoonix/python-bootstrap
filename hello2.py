#!/usr/bin/python

import sys

try:
	world = str(sys.argv[1])
	pass
except IndexError:
	world = "World!"

print "Hello, "+ world
