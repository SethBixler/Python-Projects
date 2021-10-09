#Author: Seth Bixler
#Description: Final Project
#Date: November 30 2016

#import random for random file selection.
import random


#Define function to generate the winning pick.
def generateWinningPick():

    #Generate a random integer 1,2 or 3
    ranPick = random.randrange(1,4)
    
    #If the random integer is 1, assign the winning pick to file 1 etc.
    #Create a variable that splits the winning file and returns a list.
    if ranPick == 1:
        dataOpen = open("snake.txt", "r")
        data = []
        for line in dataOpen :
            line = line.split("|")
            data.append(line)
    elif ranPick == 2:
        dataOpen = open("dog.txt", "r")
        data = []
        for line in dataOpen :
            line = line.split("|")
            data.append(line)
    elif ranPick == 3:
        dataOpen = open("cat.txt", "r")
        data = []
        for line in dataOpen :
            line = line.split("|")
            data.append(line)

    if (data == [['snake', '1']]):
        data = "snake1"
    elif (data == [['dog', '2']]):
        data = "dog2"
    elif (data == [['cat', '3']]):
        data = "cat3"
            
    #Returns the winning pick
    return data






#Define function that checks the validity of user input
def validInput(userInput):
    validInput = False

    if "snake1" in userInput:
        validInput = True

    elif "dog2" in userInput:
        validInput = True

    elif "cat3" in userInput:
        validInput = True

    else :
        validInput = False

    if validInput == True:
        return True

    elif validInput == False:
        return False
    




#Define the main function
def main():
    
    #Generate the winnng pick
    winningPick = generateWinningPick()
    
    
    #Print a welcome message explaining the rules of the game
    print("Hello! Welcome to the animal number guessing game.")
    print("Guess from the choices: snake1, dog2, or cat3." )
        
    #create a while loop that asks for user guess until they input a valid response
    validGuess = False
    while validGuess == False:

        #Prompt user to input their guess
        userInput = input("What is your guess? ")
    
        #If user input is not valid, explain why and prompt them to try again.
        validInput(userInput)
        if validInput(userInput) == False:
            print("Your input is not valid.")

        elif validInput(userInput) == True:
            validGuess = True
            break
        
    
    #Check if user input is the winning pick
    if userInput == winningPick:
        print("Congradulations, you have guessed the winning pick!")

    else:
        print("Sorry, you did not guess the winning pick.")
        print("The winning pick was", winningPick)
    



#invoke the main function
main()
    
