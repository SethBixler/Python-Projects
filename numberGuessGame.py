# Author : Seth Bixler
# Description : Number Guessing Game
# File : numberGuessGame.py
# Date : October 20, 2016

# Line 1
# Import statement
import random

# Lines 2-4
# Welcome user to the game and tell them the rules
print("Welcome to the number guessing game! The rules are as follows:")
print("A 3-digit number will be chosen at random.")
print("Your objective is to guess all 3 digits of the number, in no particular order.")

# Lines 5-9
# Ask user how many guesses they would like and save it into 'guesses'
guesses = int(input("How many guesses would you like? (Between 2-5) "))
if (guesses < 2 or guesses > 5) :
    print()
    print("You have selected an invalid amount of guesses. Game over.")
guesses = (guesses + 1)

# Lines 10-12
# Create the boolean variables
guessedOneCorrectly = False
guessedTwoCorrectly = False
guessedThreeCorrectly = False

# Lines 13-15
# Create the random numbers
randNumOne = random.randrange(0,10)
randNumTwo = random.randrange(0,10)
randNumThree = random.randrange(0,10)

# Lines 16-17
# Create a for loop that iterates as many times as the value of
# number of tries indicated by the user
if (3 <= guesses <= 6) :
    for x in range(1, guesses) :

        # Lines 18-20
        # Prompt user to provide a guess
        print()
        print("Guess number", x)
        guess = int(input("What is your guess? "))

        # Lines 21-26
        # Check to see if the guess is correct for digit number 1
        if (guessedOneCorrectly == False) :
            if (guess == randNumOne) :
                print("You have guessed the first digit")
                guessedOneCorrectly = True
            if (guess != randNumOne): 
                print("The first digit is not", guess)

        # Lines 27-32
        # Check to see if the guess is correct for digit number 2
        if (guessedTwoCorrectly == False) :
            if (guess == randNumTwo) :
                print("You have guessed the second digit")
                guessedTwoCorrectly = True
            if (guess != randNumTwo) :
                print("The second digit is not", guess)

        # Lines 33-38
        # Check to see if the guess is correct for digit number 3
        if (guessedThreeCorrectly == False) :
            if (guess == randNumThree) :
                print("You have guessed the third digit")
                guessedThreeCorrectly = True
            if (guess != randNumThree) :
                print("The third digit is not", guess)

        # Lines 39-43
        # Let user know that they won if they got all 3 digits and break the for loop
        if (guessedOneCorrectly == True and guessedTwoCorrectly == True and guessedThreeCorrectly == True) :
            print()
            print("Congradulations! You have guessed all 3 of the digits! You win!")
            print("The number was ", randNumOne,'', randNumTwo, '', randNumThree, sep='')
            break

    # Lines 44-46
    # Let user know that they lost if they did not get all three digits
    else :
        print()
        print("Sorry bud! You did not guess all three of the digits correctly. Game Over.")
        print("The number was ", randNumOne,'', randNumTwo, '', randNumThree, sep='')            
    







