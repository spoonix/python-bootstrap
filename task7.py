#!/usr/bin/python
import re

line_regex = "C.*"
sent_regex = ".*\\. C.*"
sent2_regex = ".*\\."

line_count=0
sent_count=0

with open("pg2701.txt") as file:
    for line in file:

        line_result = re.match(line_regex, line)
        sent_result = re.match(sent_regex, line)
        sent2_result = re.match(sent2_regex, line)

        if line_result != None:
            line_count += 1
            if sent_check == True:
                sent_count += 1

        if sent_result != None:
            sent_count += 1

        if sent2_result != None:
            sent_check = True
        else:
            sent_check = False


    print 'line C: ' + str(line_count)
    print 'sentence C: ' + str(sent_count)
