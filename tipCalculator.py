# Author : Seth Bixler
# Description : Tip Calculator
# File : tipCalculator.py
# Date : November 7, 2016




# Function name : promptUser
# Number of parameters :
# Returns :
def promptUser(varyingText, typeOfInput):
    userAnswer = input(varyingText)
    if (typeOfInput == "integer"):
        return int(userAnswer)
    elif (typeOfInput == "float"):
        return float(userAnswer)
   
    



def numberOfPeople():

    # calculate amount of people
    people = (adults ** 1.4) + (children ** 0.8)
    return people




def mealExpense():

    # calculate meal expenses
    if (cheapMeal < (expensiveMeal * (1/2))) :
        return expensiveMeal
    else :
        newMealExpense = ((expensiveMeal - cheapestMeal) ** (1/2))
        return newMealExpense




def sodasBill():

    # Calculate amount extra with sodas
    if (sodasConsumed < people):
        newBill = costBeforeTip + (costBeforeTip * (0.1))
    else :
        newBill = costBeforeTip + (costBeforeTip * (0.15))
    return newBill




def calcTip():
    tip = (people + newMealExpense + newBill)
    return tip
    print(tip)

    




# Function name : main
# Number of parameters : 0
def main():

    # Ask how many adults
    question = "How many adults? "
    typeOfAnswer = "integer"
    adults = promptUser(question, typeOfAnswer)
    

    # Ask how many children
    question = "How many children? "
    typeOfAnswer = "integer"
    children = promptUser(question, typeOfAnswer)
   

    # Ask what the most expensive meal was
    question = "What was the most expensive meal? "
    typeOfAnswer = "float"
    expensiveMeal = promptUser(question, typeOfAnswer)

    # Ask what the cheapest meal was
    question = "What was the cheapest meal? "
    typeOfAnswer = "float"
    cheapMeal = promptUser(question, typeOfAnswer)

    # Ask how many sodas were consumer
    question = "How many sodas were consumed? "
    typeOfAnswer = "integer"
    sodasConsumed = promptUser(question, typeOfAnswer)

    # Ask for total cost before tip
    question = "Total cost before tip? "
    typeOfAnswer = "string"
    costBeforeTip = promptUser(question, typeOfAnswer)
    


# Invoke main
main()




    
