#!/usr/bin/python
import re

def sent_counter(line):
    sent_regex = '.*[\\.\\?\\"\\!] C.*'
    sent_result = re.match(sent_regex, line)
    if sent_result != None:
        return True

def sent2_counter(line):
    sent2_regex = '.*[\\.\\?\\"\\!]'
    sent2_result = re.match(sent2_regex, line)
    if sent2_result != None:
        return True

def line_counter(line):
    line_regex = "C.*"
    line_result = re.match(line_regex, line)
    if line_result != None:
        return True

line_count=0
sent_count=0

with open("pg2701.txt") as file:
    for line in file:

        if line_counter(line):
            line_count += 1
            if sent2_counter(line):
                sent_count += 1

        if sent_counter(line):
            sent_count += 1


    print 'line C: ' + str(line_count)
    print 'sentence C: ' + str(sent_count)
