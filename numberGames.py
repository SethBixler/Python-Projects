# Author : Seth Bixler
# Description : Number Guessing Game
# File : numberGames.py
# Date : October 18, 2016

# Line 1
# 1. import statement
import random 

# Lines 2-3
# 2. print salutation
print("Let us play a guessing game.")
print("First you must select a range from which I'll select a random number.")

# Lines 4-5
# 3. prompt user for lower and upper bounds
lowBound = int(input("What is the lower bound? "))
upBound = int(input("What is the upper bound "))

# Lines 6-7
# 4. check if upper and lower bounds differ by at least 10
# If not, then print an error message
if ((upBound - lowBound) < 10) :
    print("The numbers you selected are not at least 10 integers apart...quitting.")

# Line 8
# otherwise
else :

    # Lines 9-10
    # 5. prompt user for how many guesses are desired
    guesses = int(input("How many guesses would you like? "))
    guesses = (guesses + 1)
    
    # Line 11
    # 6. create a boolean variable guessedCorrectly
    guessedCorrectly = False
                  
    # Line 12
    # 7. generate a random number and save it into a variable
    randomNum = random.randrange(lowBound, upBound)
                  
    # Lines 13-14
    # 8. print status message
    print("I have created a random number between", lowBound, "and", upBound)
    print("Let us begin. Good luck, and have fun!")
    
    # Line 15
    # 9. create a for loop that iterates as many times as the value
    # of tries indicated by user
    for x in range(1, guesses) :

        # Line 16
        # 10. Print the guess number
        print("Guess number", x)

        # Line 17
        # 11. Prompt user to provide a guess, and save into variable
        guess = int(input("What is your guess? "))

        # Lines 18-20
        # 12. Check if guess is the same as randomly generated number.
        # If so, print "win", update variable guessedCorrectly so that
        # it is true, and force exit out of the for loop
        if (guess == randomNum) :
            print("That's correct! You win!")
            guessedCorrectly = True
            break

        # Lines 21-22
        # 13. If the guess is NOT the same as the randomly generated
        # number then print "try again"
        else :
            print("That is incorrect, try again.")

    # Lines 23-25    
    # 14. After the for loop terminates check if the variable
    # guessedCorrectly is not True. If it is not true, print
    # you lose and specify the correct answer
    if (guessedCorrectly == False) :
        print("Sorry Charlie, you lose.")
        print("The correct number was", randomNum)
