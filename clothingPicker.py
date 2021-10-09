# Author : Seth Bixler
# Description : Lab 3, CSCI 141
# File : clothingPicker.py
# Date : October 11, 2016

# Lines 1-5
# Ask the user if it is windy
# Receive input from user and save into a variable
# If it windy, output "Be sure to not bring an umbrella because it is windy."
# If it is not windy, output "It is not windy, bring an umbrella if you please."
isWindy = (input("Is it windy? (yes or no) "))
if (isWindy == "yes") :
    print("Be sure not to bring an umbrella because it is windy.")
else :
      print("It is not windy, bring an umbrella if you please.")

# Lines 6-11
# Ask the user if it is windy
# Receive input from user and save into a variable
# Ask the user if it is sunny
# Receive input from user and save into a variable
# If it is both windy and sunny, output "It is windy and sunny, so don't bring a umbrella and wear a coat."
# If it is not both windy and sunny, outut "It is not both windy and sunny."
isWindy = (input("Is it windy? (yes or no) "))
isSunny = (input("Is it sunny? (yes or no) "))
if (isWindy == "yes" and isSunny == "yes") :
    print("It is windy and sunny, so don't bring a umbrella and wear a coat.")
if (isWindy == "no" or isSunny == "no") :
     print("It is not both windy and sunny.")

# Lines 12-21
# Ask the user if it is windy
# Receive input from user and save into a variable
# Ask the user if it is sunny
# Receive input from user and save into a variable
# If it is both windy and sunny, output "It is windy and sunny."
# If it is windy and not sunny, output "It is windy and not sunny."
# If it is sunny and not windy, output "It is sunny and not windy."
# If it is neither sunny nor windy, output "It is neither sunny nor windy."
isWindy = (input("Is it windy? (yes or no) "))
isSunny = (input("Is it sunny? (yes or no) "))
if (isWindy == "yes" and isSunny == "yes") :
    print("It is windy and sunny.")
if (isWindy == "yes" and isSunny == "no") :
    print("It is windy and not sunny.")
if (isWindy == "no" and isSunny == "yes") :
    print("It is sunny and not windy.")
if (isWindy == "no" and isSunny == "no") :
    print("It is neither sunny nor windy.")

# Lines 22-37
# Ask the user if it is sunny
# Receive input from the user and save into a variable
# Ask user what the temperature is
# Receive input from the user and save into a variable
# If it is sunny and less than 60 degrees, output "Wear a sweater."
# If it is sunny and 60 degrees exactly, output "Woo hoo, it is 60 degrees. Wear what you want."
# If it is sunny and more than 60 degrees, output "Wear a tee shirt and flip flops."   
# If it is not sunny and less than 40 degress, output "Wear a coat and hat."
# If it is not sunny and between 40 and 50 degrees, output "Not quite freezing, but close. Bundle up."
# If it is not sunny and 50 degrees exactly, output "A jacket is best."
# If it is not sunny and more than 50 degrees, output 
isSunny = (input("Is it sunny? (yes or no) "))
temp = (input("What is the temperature? (enter integer in degrees fahrenheit) "))
if (isSunny == "yes" and temp < "60") :
    print("Wear a sweater.")
if (isSunny == "yes" and temp == "60") :
    print("Woo hoo, it is 60 degrees. Wear what you want.")
if (isSunny == "yes" and temp > "60") :
    print("Wear a tee shirt and flip flops.")
if (isSunny == "no" and temp < "40") :
    print("Wear a coat and hat.")
if (isSunny == "no" and "40" <= temp < "50") :
    print("Not quite freezing, but close. Bundle up.")
if (isSunny == "no" and temp == "50") :
    print("A jacket is best.")
if (isSunny == "no" and temp > "50") :
    print("Wear a long sleeved shirt.")
    


    
    
     

      

