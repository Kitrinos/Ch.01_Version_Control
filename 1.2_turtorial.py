'''
# Modify the starter code below to create your own cool drawing
# and then Pull Request it to your instructor.

# Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''

# turtle.exitonclick() #Keeps pycharm window open

import turtle
toka = turtle.Turtle()

toka.shape('turtle')
screen=turtle.Screen() #makes screen an object
screen.bgcolor('black')

toka.speed(10) #the drawing speed

#the bottom
toka.color('green')
toka.penup()
toka.begin_fill()
toka.goto(-200,-120)
toka.forward(400)
toka.right(90)
toka.forward(90)
toka.right(90)
toka.forward(400)
toka.right(90)
toka.forward(90)
toka.end_fill()
toka.right(90)
toka.forward(200)
toka.left(90)
toka.forward(150)
toka.right(90)
#needed this to commmit the code
#this is the triange
toka.begin_fill()
toka.color('light blue')
toka.right(60)
toka.forward(200) # draw base
toka.right(120)
toka.forward(200)
toka.right(120)
toka.forward(200)
toka.end_fill()
toka.color('blue')
toka.left(-60)

toka.goto(0,-20)

#this is the circle
toka.begin_fill()
toka.color('grey')
toka.circle(90)
toka.end_fill()

#turtle first plip
toka.penup()
toka.color('blue')
toka.goto(50,70)
toka.pendown()
toka.begin_fill()
toka.color('dark grey')
toka.circle(20)
toka.end_fill()

#the second plip
toka.color('blue')
toka.penup()
toka.goto(50,40)
toka.begin_fill()
toka.color('dark grey')
toka.circle(10)
toka.end_fill()

#the smallest plip
toka.penup()
toka.begin_fill()
toka.color('dark grey')
toka.goto(30,120)
toka.circle(10)
toka.end_fill()
toka.penup()
#erases toka
toka.color('grey')
toka.goto(-150,50)
toka.write('Nellie Leaverton',font=("Arial", 12, "normal"))

turtle.exitonclick() #Keeps pycharm window open