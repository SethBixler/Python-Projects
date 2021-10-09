# Author : Seth Bixler
# Description : Turtle Module
# File : followTheTurtle.py
# Date : November 3, 2016



# Import the turtle module
import turtle

# Create graphics window
wn = turtle.Screen()

# Set background color as light green
wn.bgcolor("lightgreen")




# Create a blue turtle named 'mom'
mom = turtle.Turtle()
mom.color("red")
mom.shape("turtle")

# Give 'mom' her directions
print(range(5,120,2))
for size in range(5,120,2):
    mom.stamp()
    mom.forward(size)
    mom.right(24)

    


# Create a green turtle named 'son1'
son1 = turtle.Turtle()
son1.color("green")
son1.shape("turtle")

# Give 'son1' his directions
son1.up()
son1.right(90)
son1.forward(10)
son1.left(90)
print(range(5,120,2))
for size in range(5,120,2):
    son1.stamp()
    son1.forward(size)
    son1.right(24)




# Create a green turtle named 'son2'
son2 = turtle.Turtle()
son2.color("blue")
son2.shape("turtle")

# Give 'son2' his directions
son2.up()
son2.right(90)
son2.forward(20)
son2.left(90)
print(range(5,120,2))
for size in range(5,120,2):
    son2.stamp()
    son2.forward(size)
    son2.right(24)







  
