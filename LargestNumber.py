"""
R. Scott Harrington
05/15/2020

Repeatedly prompt a user for integers until the user enters '-1'. Once '-1' is
entered, print out the largest/smallest of numbers. 

"""
# -*- coding: utf-8 -*-

import math

numList = []		# empty list to hold input
notDone = True		# bool to determine done or not

while notDone:
	num = input("Enter a number ('-1' to exit): ")
	numList.append(int(num))				# convert input to integer + add
	if num == '-1' :
		numList.pop(len(numList) - 1)		# remove '-1' from list
		#sanity check
		print('All done! Calculating stuff below\n')
		break
	else :
		print('Not done... keep going')

print('This is your list', sorted(numList))

largest = max(numList)
smallest = min(numList)
print('Largest:', largest)
print('Smallest:', smallest)
