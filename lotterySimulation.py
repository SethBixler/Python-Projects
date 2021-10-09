# Author : Seth Bixler
# Description : Lottery Simulation
# File : lotterySimulation.py
# Date : Novemeber 8, 2016





# import the random module
import random





# Generate the "winning" pick, which is
# a word and the digit 1, 2 or 3. The word
# or digit can be first
def generateWinningPick():

    # generate the random integer 1, 2 or 3
    aRandomInteger = random.randrange(1,4)

    # Select one of three words, and return
    # the winning pick, which is a concatenation
    # of the word and the str equivalent
    # of aRandomInteger
    anotherRandomNum = random.randrange(1,6)
    if (anotherRandomNum == 1):
        return "monkey" + str(aRandomInteger)
    elif (anotherRandomNum == 2):
        return "dragon" + str(aRandomInteger)
    elif (anotherRandomNum == 3):
        return "snake" + str(aRandomInteger)
    elif (anotherRandomNum == 4):
        return str(aRandomInteger) + "dragon"
    elif (anotherRandomNum == 5):
        return str(aRandomInteger) + "monkey"
    else:
        return str(aRandomInteger) + "snake" 





# the main function
def main():


    # generate the winning lottery pick
    winningPick = generateWinningPick()


    # print welcome message
    print("Lottery pic checker V1.2. Let's see if you've won")
    print("a fabulous prize. The word choices were monkey,")
    print("dragon, and snake, and digit choices were 1, 2 or 3.")
    print("The winning pick is a word and digit, in any order.")


    # Prompt user to input their guess
    possibleGuess = True
    while (possibleGuess == True) :
        userGuess = str(input("What word/number combination did you select? "))

    
    # While user’s input is not valid, explain why input
    # is bad and prompt again
        
        if ("monkey") in userGuess :
            if ("1") in userGuess :
                possibleGuess = False
                break
            if ("2") in userGuess :
                possibleGuess = False
                break
            if ("3") in userGuess :
                possibleGuess = False
                break
        if ("dragon") in userGuess :
            if ("1") in userGuess :
                possibleGuess = False
                break
            if ("2") in userGuess :
                possibleGuess = False
                break
            if ("3") in userGuess :
                possibleGuess = False
                break
        if ("snake") in userGuess :
            if ("1") in userGuess :
                possibleGuess = False
                break
            if ("2") in userGuess :
                possibleGuess = False
                break
            if ("3") in userGuess :
                possibleGuess = False
                break
        else :
            print("Your input MUST contain one of the words monkey, dragon, or snake,")
            print("as well as a number 1, 2, or 3.")
        

    # Declare variables numEntered and wordEntered and initialize
    # to the empty string
    numEntered = ""
    wordEntered = ""


    # If the first character of user’s input is the string 1, 2 or 3
    if (userGuess[0] == "1") :
    
        # Set the values for numEntered and wordEntered using [ ]
        numEntered = (userGuess[0])
        wordEntered = (userGuess[1:])


    elif (userGuess[0] == "2") :
    
        # Set the values for numEntered and wordEntered using [ ]
        numEntered = (userGuess[0])
        wordEntered = (userGuess[1:])


    elif (userGuess[0] == "3") :
    
        # Set the values for numEntered and wordEntered using [ ]
        numEntered = (userGuess[0])
        wordEntered = (userGuess[1:])
        

    # If the last character of user’s input is the string 1, 2 or 3
    elif (userGuess[-1] == "1") :

        # Set the values for numEntered and wordEntered using [ ]
        numEntered = (userGuess[-1])
        wordEntered = (userGuess[0:-1])


    elif (userGuess[-1] == "2") :

        # Set the values for numEntered and wordEntered using [ ]
        numEntered = (userGuess[-1])
        wordEntered = (userGuess[0:-1])


    elif (userGuess[-1] == "3") :

        # Set the values for numEntered and wordEntered using [ ]
        numEntered = (userGuess[-1])
        wordEntered = (userGuess[0:-1])   


    # Check if the user's input matches exactly the winning pick
    if (userGuess == winningPick) :
        print("Congradulations! You picked the winning word and number!")
        print("The winning pick was", winningPick)

      
    # Check if user’s word and number are in the winning pick
    if (wordEntered in winningPick) :
        if (numEntered in winningPick) :
            print("Congradulations! You picked the winning word and number!")
            print("The winning pick was", winningPick)
    

    # Else check if user’s word but not number are in the winning pick
    elif (wordEntered in winningPick) :
        if (numEntered not in winningPick) :
            print("You guessed the right word but not the right number.")
            print("The winning pick was", winningPick)


    # Else check if user’s number but not word are in the winning pick
    elif (numEntered in winningPick) :
        if (wordEntered not in winningPick) :
            print("You guessed the right number but not the right word.")
            print("The winning pick was", winningPick)
           

    # Else print "You guessed neither the word nor number"
    else :
        print("You guessed neither the word nor number.")
        print("The winning pick was", winningPick)
 


    
    

# Invoke the main function    
main()






