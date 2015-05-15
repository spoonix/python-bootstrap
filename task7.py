#!/usr/bin/python
import re

def sentence_verify(line):
    sent_regex = re.compile('\w+[\.\?\!]+\W+$')
    sent_result = sent_regex.search(line)
    if sent_result != None:
        return True

def sentence_counter(line):
    sent_regex = re.compile('\w+[\.\?\!]+\W+C')
    sent_result = sent_regex.search(line)
    if sent_result != None:
        return True

def line_counter(line):
    sent_regex = re.compile('^C')
    sent_result = sent_regex.search(line)
    if sent_result != None:
        return True

sent_c = 0
line_c = 0

with open("pg2701.txt") as file:
    for line in file:

        if sentence_counter(line):
            sent_c += 1

        if line_counter(line):
            line_c += 1
            if sentence_verify(line):
                sent_c += 1

        if sentence_verify(line):
            sent_ver = True
        else:
            sent_ver = False

print 'Sentence C: ' + str(sent_c)
print 'Line C: ' + str(line_c)
