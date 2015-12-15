"""
R. Scott Harrington
This program repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, prints out the largest of the numbers. 
12/15/2015
"""
# -*- coding: utf-8 -*-

numList = []			# empty list to hold input
notDone = True		# bool to determine number or not

while notDone :
	num = raw_input("Enter a number: ")	
	numList.append(num)
	if num == 'done' :
		numList.pop(len(numList) - 1)			# remove 'done' from list
		#sanity check
		print 'All done! Calculating stuff below\n'
		break
	else :
		print 'Not done... keep going'

print 'This is your list', numList

largest = None
for newNum in numList :
	if largest is None or newNum > largest :
		largest = newNum
print 'Largest', largest