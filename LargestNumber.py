"""
R. Scott Harrington
This program repeatedly prompts a user for integer numbers until the user enters
'done'. Once 'done' is entered, prints out the largest of the numbers. 
05/15/2020
"""
# -*- coding: utf-8 -*-

numList = []		# empty list to hold input
notDone = True		# bool to determine done or not

while notDone:
	num = input("Enter a number (done to exit): ")
	numList.append(num)
	if num == 'done' :
		numList.pop(len(numList) - 1)		# remove 'done' from list
		#sanity check
		print('All done! Calculating stuff below\n')
		break
	else :
		print('Not done... keep going')

print('This is your list', numList)

largest = None
for newNum in numList :
	if largest is None or newNum > largest :
		largest = newNum
print('Largest', largest)
