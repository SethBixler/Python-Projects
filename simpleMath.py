# Author : Seth Bixler
# Description : Simple Calculator
# File : simpleMath.py
# Date : October 25 2016

# Import statement
import random

# Function printSalutation
# Input : a perons's name
# Returns : nothing
def printSalutation(aName):

    # Print a personalized welcome message with instructions
    print()
    print("Welcome ", aName, "!", sep="")
    print("Let's practice your addition, multiplication, and subtraction!")
    print("Once you begin, you may type -1 to quit.")

# Prompt the user to input their name
personsName = input("Hi. What is your name? ")
printSalutation(personsName)

# Prompt the user to specify what type of math questions they would like,
# and saves into the variable 'qType'
print()
qType = input("What type of math questions would you like? (a, s, or m) ")

# Function : displayAdditionQuestion
# Input : nothing
# Returns : a number
def displayAdditionQuestion():

    # Declare the variable 'num1' and assign it a random number between 0 and 9
    num1 = random.randrange(0, 10)

    # Declare the variable 'num2' and assign it a random number between 0 and 9
    num2 = random.randrange(0, 10)
   
    # Print the addition question using the just created variables
    print("What is", num1, "+", num2, "? ")

    # Return the summation of num1 and num2
    return num1 + num2

# Invocation of function
# Create a while loop that will continue to output addition questions until
# the user enters '-1'
continuePlaying = True
while (continuePlaying) :
    if (qType == "a") :
        print("==================")
        correctAnswer = displayAdditionQuestion
        userAnswer = int(input("What is you answer? "))
        if (userAnswer == -1) :
            continuePlaying = False;
            break
        if (userAnswer == correctAnswer) :
            print("Good job, that is correct.")
        else :
            print("Good try, but that is incorrect.")
            print("The correct answer was", correctAnswer, '.', sep='')
