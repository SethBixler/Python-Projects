# Author : Seth Bixler
# Description : DJ Name Creator
# File : DJName.py
# Date : Novemeber 14, 2016





# Generate DJ name which is the first half
# of the user's first name and last half
# of the user's last name, with sizzle on the end
def generateDJName(userName):

    # Split name up
    aList = userName.split()
    firstName = (aList[0])
    lastName = (aList[1])

    # Take out first half of first name
    halfLengthOfFirstName = (len(firstName) // 2)
    firstHalfOfFirstName = firstName[0:halfLengthOfFirstName]

    # Create first part of DJ name
    firstPartOfDJName = firstHalfOfFirstName

    # Take out second half of last name
    halfLengthOfLastName = ((len(lastName) + 1) // 2)
    secondHalfOfLastName = lastName[halfLengthOfLastName:len(lastName)]

    # Create second part of the DJ name
    secondPartOfDJName = secondHalfOfLastName

    # Add 'sizzle' to the end of the DJ name
    DJName = (firstPartOfDJName, secondPartOfDJName, "sizzle")
    return DJName







# Check to see if the input is valid
def isInputValid(userName):

    # Set validInput to false
    validInput = False

    # Check if there is numbers in userName
    for x in range(0,10):
        if (str(x) not in userName) :
            validInput = True
        
    # Check to make sure there is a single blank space in userName
    if " " in userName :
        validInput = True

    # Check to make sure there is at least 5 characters
    if (len(userName) > 4) :
        validInput = True

    # Return boolean value
    if (validInput == True):
        return True
    else :
        return False






# The main function
def main():

    
    # Print a welcome message
    print("Welcome to the DJ name creator!")

    # Create a while loop to get a user name
    validInput = False
    while (validInput == False):
    
        # Ask user to input first and last name
        userName = input("What is your first and last name? ")

        # Check to see if input is valid
        if (isInputValid(userName) == True) :
            break
        else :
            print("Incorrect input, please try again.")
        

    # Invoke generateDJName custom function
    DJName = generateDJName(userName)

    # Print DJ name
    print("Your DJ name is : ", DJName)
    





# Invoke the main function
main()
