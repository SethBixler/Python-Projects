# Author : Seth Bixler
# Description : Home Square-Footage Calculator
# File : homeSquareFootageCalculator
# Date : Novemeber 1, 2016



# Function name : promptUser
# Number of parameters : 2
def promptUser(varyingText, typeOfInput):
    userAnswer = input(varyingText)
    if (typeOfInput == "integer"):
        return int(userAnswer)
    elif (typeOfInput == "string"):
        return str(userAnswer)
   
        


# Function name : calcRoomSquareFootage
# Number of parameters : 1
# Returns : a number
def calcRoomSquareFootage(roomShape):

    # If the shape of the room is square, prompt the user to input the
    # dimension via invoking the function the promptUser function. Return
    # the room's size
    if(roomShape == "square"):
        question = "What is the side length of the square room? "
        typeOfAnswer = "integer"
        squareSideLength = promptUser(question, typeOfAnswer)
        squareArea = (squareSideLength ** 2)
        return squareArea

    # If the shape of the room is a rectangle, prompt the user to input the
    # the first and second dimension using the promptUser function. Return
    # the product of both dimensions
    if(roomShape == "rectangle"):
        question = "What is the length of the first dimension? "
        typeOfAnswer = "integer"
        rectSideLength1 = promptUser(question, typeOfAnswer)
        question = "What is the length of the second dimension? "
        typeOfAnswer = "integer"
        rectSideLength2 = promptUser(question, typeOfAnswer)
        rectArea = (rectSideLength1 * rectSideLength2)
        return rectArea

# Function name : main
def main():

    # Prompt the user for the number of rooms in the house
    numberOfRooms = int(input("What is the number of rooms? "))

    # Create a variable for holding the running total of the square
    # footage of the house; initialize to the value 0
    totalSquareFootage = calcRoomSquareFootage(1)
    

    # For as many rooms as the user has indicated that there are, ask
    # for the shape of the room using the promptUser function. The return
    # value of promptUser should be provided as the input argument to
    # calcRoomSquareFootage.
    for x in range(1, numberOfRooms + 1):
        roomShape = input("What is the shape of room "+ str(x)+ ", square or rectangle? ")
        calcRoomSquareFootage(roomShape)
        return roomShape

    # Print the total square footage of the house
    print(totalSquareFootage)


# Invoke the main function
main()
