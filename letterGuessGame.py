# Author : Seth Bixler
# Description : Letter Guessing Game
# File : letterGuessingGame.py
# Date : October 20, 2016

# Line 1
# Import statement
import random

# Lines 2-4
# Welcome user to the game and tell them the rules
print("Welcome to the letter guessing game! The rules of the game are simple.")
print("Two letters among the word 'bellingham' will be chosen at random.")
print("Your goal is to guess both of those letters in your allotted number of guesses.")

# Lines 5-8
# Ask user how many guesses they would like and record into a variable
guesses = int(input("How many guesses would you like? (Between 2-4) "))
if (guesses < 2 or guesses > 4) :
    print()
    print("You have selected an invalid amount of guesses. Game over.")

# Lines 9-10
# Create the boolean variable
guessedOneCorrectly = False
guessedTwoCorrectly = False

# Lines 11-12
# Create random numbers
randNumOne = random.randrange(0,10)
randNumTwo = random.randrange(0,10)

# Lines 13-52
# Turn the numbers into letters of the word 'bellingham'
if (randNumOne == 0) :
    randNumOne = ("b")
if (randNumTwo == 0) :
    randNumTwo = ("b")

if (randNumOne == 1) :
    randNumOne = ("e")
if (randNumTwo == 1) :
    randNumTwo = ("e")

if (randNumOne == 2) :
    randNumOne = ("l")
if (randNumTwo == 2) :
    randNumTwo = ("l")

if (randNumOne == 3) :
    randNumOne = ("l")
if (randNumTwo == 3) :
    randNumTwo = ("l")

if (randNumOne == 4) :
    randNumOne = ("i")
if (randNumTwo == 4) :
    randNumTwo = ("i")    

if (randNumOne == 5) :
    randNumOne = ("n")
if (randNumTwo == 5) :
    randNumTwo = ("n")

if (randNumOne == 6) :
    randNumOne = ("g")
if (randNumTwo == 6) :
    randNumTwo = ("g")

if (randNumOne == 7) :
    randNumOne = ("h")
if (randNumTwo == 7) :
    randNumTwo = ("h")

if (randNumOne == 8) :
    randNumOne = ("a")
if (randNumTwo == 8) :
    randNumTwo = ("a")

if (randNumOne == 9) :
    randNumOne = ("m")
if (randNumTwo == 9) :
    randNumTwo = ("m")   

# Lines 53-54
# Create a for loop that itirates as many times as the value 'guesses' was chosen
if (2 <= guesses <=4) :
    for x in range(0, guesses) :

        # Lines 55-57
        # Print guess number and ask user what their guess is and save into a variable
        print()
        print("Guess number", (x + 1))
        guess = input("What is your guess? ")

        # Lines 56-61
        # Check to see if the guess is correct for letter 1
        if (guessedOneCorrectly == False) :
            if (guess == randNumOne) :
                print("You have guessed the first letter")
                guessedOneCorrectly = True
            if (guess != randNumOne) :
                print("The first letter is not", guess)

        # Lines 62-67
        # Check to see if the guess is correct for letter 2
        if (guessedTwoCorrectly == False) :
            if (guess == randNumTwo) :
                print("You have guessed the second letter")
                guessedTwoCorrectly = True
            if (guess != randNumTwo) :
                print("The second letter is not", guess)

        # Lines 68-72
        # Let user know that they won if they guessed the 2 letters and break the loop
        if (guessedOneCorrectly == True and guessedTwoCorrectly == True) :
            print()
            print("Congradulations, you have guessed both of the letters! You win!")
            print("The letters were", randNumOne, "and", randNumTwo)
            break

    # Lines 73-76
    # Let user know that they lost if they did not guess both of the letters
    else :
        print()
        print("Dang! You did not guess both of the letters correctly. Game over.")
        print("The letters were", randNumOne, "and", randNumTwo)



