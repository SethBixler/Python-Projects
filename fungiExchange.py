# Author : Seth Bixler
# Description : Coding Homework 2
# File : fungiExchange.py
# Date : October 12, 2016

# Lines 1-2
# Ask user how many shitake they found
# Receive input and save into variable shit
# Ask user how many portebella they found
# Receive input and save into variable port
shit = int(input("How many shitake did you find on your trek? "))
port = int(input("How many portebella did you find on your trek? "))

# Lines 3-5
# Tell user "As you travel through the forest, you encounter a soup chef."
# Tell user "The chef asks you, how many shitake would you like to trade? "
# Receive input and save into variable shitTrade
# Tell user "How many portebella would you like tyo trade? "
# Receive input and save into variable portTrade
print("As you travel through the forest, you encounter a soup chef.")
shitTrade = int(input("The chef asks you, how many shitake would you like to trade? "))
portTrade = int(input("How many portebella would you like to trade? "))

# Lines 6-17
# Output the amount of rubies offered in the trade
if (shitTrade > shit or portTrade > port) :
    print("You don't have that many mushrooms, so how do you expect to trade me?")
if (shitTrade == 0 and portTrade == 0) :
    print("You cannot trade me with imaginary mushrooms.")
if (0 < shitTrade < 10 and 0 < portTrade < 5 and shitTrade < shit and portTrade < port) :
    trade = shitTrade * 2
    print("The chef says, I will offer you", shitTrade * 2, "rubies.")
if (shitTrade < 10 and portTrade >= 5 and shitTrade < shit and portTrade < port) :
    trade = portTrade * 3
    print("The chef says, I will offer you", portTrade * 3, "rubies.")
if (shitTrade % 12 == 0 and shitTrade % 24 != 0 and portTrade >= 20 and shitTrade < shit and portTrade < port) :
    trade = portTrade * 4
    print("The chef says, I will offer you", portTrade * 4, "rubies.")
if (shitTrade % 12 == 0 and shitTrade % 24 != 0 and portTrade <= 20 and shitTrade < shit and portTrade < port) :
    trade = portTrade
    print("The chef says, I will offer you", portTrade, "rubies.")
else :
    trade = shitTrade * 5
    print("The chef says, I will offer you", shitTrade * 5, "rubies.")

# Lines 18-22
# Ask user if they will accept the trade
# Send the user away with the amount of rubies and mushrooms based on if they make the trade or not
if (trade > 0) :
    yOn = input("Do you accept the trade? (yes or no) ")
    if (yOn == "yes") :
        print("You make the trade! You walk away with", trade, "rubies,", shit - shitTrade, "shitake mushroom(s), and", port - portTrade, "portabella mushroom(s). Soup Time!")
    if (yOn == "no") :
        print("You do not make the trade. You walk away with 0 rubies,", shit, "shitake mushroom(s), and", port, "portabella mushroom(s).")
