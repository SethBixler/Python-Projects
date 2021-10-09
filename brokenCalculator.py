# Author : Seth Bixler
# Description : Lab 2, CSCI 141
# File : brokenCalculator.py
# Date : October 4, 2016

# Lines 1-2
# Get the first and second integers
firstInput = int(input("Please enter the first integer "))
secondInput = int(input("Please enter a second integer "))

# Line 3
# Print out "Fixing notation!"
print("Fixing notation!")

# Lines 4-5
# Extract the integer and decimal portions from the first integer input
firstInt = (firstInput // 10)
firstDec = (firstInput % 10)

# Line 6
# Print the reformatted first input
print("The value ", firstInput, " has been reformatted to ", firstInt, ".", firstDec, sep="")

# Lines 7-8
# Extract the integer and decimal portions from the second integer input
secondInt = (secondInput // 10)
secondDec = (secondInput % 10)

# Line 9
# Print the reformatted second input
print("The value ", secondInput, " has been reformatted to ", secondInt, ".", secondDec, sep="")

# Lines 10-14
# Perform calculations for the product of the reformatted (decimal) values
firstIntTimesSecondInt = (firstInt * secondInt)
firstIntTimesSecondDec = (firstInt * secondDec * 0.1)
secondIntTimesFirstDec = (secondInt * firstDec * 0.1)
firstDecTimesSecondDec = (firstDec * secondDec * 0.01)
total = (firstIntTimesSecondInt + firstIntTimesSecondDec + secondIntTimesFirstDec + firstDecTimesSecondDec)

# Line 15
# Print out the final result
print("The product of ", firstInt, '.', firstDec, " and ", secondInt, '.', secondDec, " is ", total, sep='')
