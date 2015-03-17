#!/usr/bin/python

def medianate(list):
	for number in list:
		new_number = float(number) + 0.5
		print new_number
	return new_number
	
def lensort(list2):
	for i in sorted(list2, key=len, reverse=True):
    		print i


medianate([1, 2, 3.3])

lensort(['abc', 'abcd', 'abaaa', 'a'])