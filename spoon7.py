#!/usr/bin/python

import re

f = open("pg2701.txt")

line_regex = "([\"\'])?C"
sent_regex = "[\.\?\!]([\'\"])?\s+C"

lcnt = 0
scnt = 0
last_char = "."

for l in f.readlines():
    line = l.rstrip()
    if len(line) > 0:
        last_char = line[-1]
    else:
        last_char = " "
    if re.match( line_regex, line ):
        #print "Line: %s" % line
        lcnt = lcnt + 1

    if re.match("[\.\?\!]([\'\"])?", last_char) and re.match( line_regex, line):
        #print "Sent: %s" % line
        scnt = scnt + 1
    elif re.search(sent_regex, line ):
        #print "Sent: %s" % line
        scnt = scnt + 1
    

print "Line count: %d" % lcnt
print "Sent count: %d" % scnt
