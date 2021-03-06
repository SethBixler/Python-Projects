# Author : Seth Bixler
# Description : People lists and Files
# File : peopleAndItems.py
# Date : Novemeber 15, 2016





# import functionality to copy lists with sublists
from copy import deepcopy


# the template list with 4 sublists
template = ["name",["works"],["coins"],["bills"],["misc"]]


# list that will hold user data lists (the inventory)
# this is originally an empty list
stats = [ ]


# counter to keep track of how many files have been processed
counter = 0


# continue to prompt user to supply file names
while True :


    # get the file name
    filename = input("File name to parse ")


    # if user inputs "done" then exit while loop
    if filename == "done" :
        break


    # TO DO 1 : creating a pointer to a file
    #
    # Create a variable, fileInput, that points to
    # the file specified by the user and that was saved
    # to the variable filename. The file should be
    # opened for reading.
    #
    # WRITE YOUR CODE HERE - 1 line
    fileInput = open(filename, "r")




    
    # extract lines from the file; the loop variable
    # line is of type string
    for line in fileInput:

    
        # TO DO 2 : use of split
        #
        # Create a new variable, words, and assign
        # it the output of split() when it is used
        # on the variable line. Refer to the lecture
        # slides and recall that split() returns a list.
        #
        # WRITE YOUR CODE HERE - 1 line
        words = line.split()






        # Check if the first word of the line is the
        # word "works"
        if words[0] == "works" :


            # Use the join function (refer to lecture
            # slides) to create a string that is made up
            # of all remaining items in the list works.
            # This is being provided for you.
            workTitle = " ".join(words[1:])


            # Append to the stats list, at index position 1
            # the name of the work.
            stats[counter][1].append(workTitle)


        # Check if the first word of the line is the
        # word "coins"
        elif words[0] == "coins" :


            # Retrieve sucessive elements from the list
            # words, and convert each one to an int,
            # and then append to the stats list
            # at index position 2. Because each "coins"
            # line has exactly 4 digits, words[1] refers
            # to the count of pennies, words[2] refers
            # to the count of nickels, etc.
            stats[counter][2].append(int(words[1]))
            stats[counter][2].append(int(words[2]))
            stats[counter][2].append(int(words[3]))
            stats[counter][2].append(int(words[4]))


        # if the first word is "bills"
        elif words[0] == "bills" :


            # TO DO 3 : processing a "bills" line
            #
            # Retrieve sucessive elements from the list
            # words, and convert each one to an int,
            # and then append to the stats list
            # at index position 3. Follow the example
            # for the coins (above), but remember
            # that each "bills" line in a text file
            # has 6 numbers instead of 4
            #
            # WRITE YOUR CODE HERE - 6 lines
            stats[counter][3].append(int(words[1]))
            stats[counter][3].append(int(words[2]))
            stats[counter][3].append(int(words[3]))
            stats[counter][3].append(int(words[4]))
            stats[counter][3].append(int(words[5]))
            stats[counter][3].append(int(words[6]))





        # if the first word is "misc"
        elif words[0] == "misc" :


            # Use the join function (refer to lecture
            # slides) to create a string that is made up
            # of all remaining items in the list words.
            miscItem = " ".join(words[1:])


            # Append to the stats list, at index position 4
            # the misc. item.
            stats[counter][4].append(miscItem)


        # else the single word should be the user's name
        elif len(words[0]) > 0 :


            # Create a new list that is a copy of
            # the template list.
            newUser = deepcopy(template)


            # Append to the stats list the just-created
            # newUser list.
            stats.append(newUser)


            # The value of index position 0 of the just-created
            # list should have the name of the user.
            stats[counter][0] = words[0]


    # increment the number of files that have been processed
    counter = counter + 1


# TO DO 4 : calculate and print the total "money" among all people info
# whose files have been processed
#
# WRITE YOUR CODE HERE - fewer than 20 lines
for x in range(0, counter):
    sumCoins = (((stats[x][2][1]) * .01) + ((stats[x][2][2]) * .05) + ((stats[x][2][3]) * .1)
                + ((stats[x][2][4]) * .25))
    sumBills = (((stats[x][3][1]) * 1) + ((stats[x][3][2]) * 5) + ((stats[x][3][3]) * 10)
                + ((stats[x][3][4]) * 20) + ((stats[x][3][5]) * 50) + ((stats[x][3][6]) * 100))
print("Bills and Coins :", sumCoins + sumBills)
    













# TO DO 5 : retreive from the user list (and sublists) the names of
# the work(s) that have been authored/created by the person(s) whose
# data files were processed, separated by commas.
#
# WRITE YOUR CODE HERE - fewer than 5 lines
for x in range(0, counter):
    for y in range(1, len(stats[x][1])):
        print("Works :", (stats[x][1][y]))







# TO DO 6 : retreive from the user list (and sublists)
# the misc items of the 4 people. Output the list of misc items,
# separated by commas.
#
# WRITE YOUR CODE HERE - fewer than 5 lines
for x in range(0, counter):
    for y in range(1, len(stats[x][4])):
        print("Misc. Items :", (stats[0][4][y]))











