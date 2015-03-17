#!/usr/bin/python

import os.path
import sys

path = str(sys.argv[1])

if os.path.isfile(path) == False:
	sys.stderr.write('ERROR: File doesent exist \n')
	sys.exit(73)

f = open(path, 'r')
file_forward = f.read()
print file_forward
f.close()

print "\n"
for line in reversed(open(path).readlines()):
    print line.rstrip()
