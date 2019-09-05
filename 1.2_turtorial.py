'''
# Modify the starter code below to create your own cool drawing
# and then Pull Request it to your instructor.

# Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
# turtle.exitonclick() #Keeps pycharm window open

# import turtle
# toka = turtle.Turtle()
# toka.shape('turtle')
# screen=turtle.Screen() #makes screen an object
# screen.bgcolor('white')
#
# toka.speed(10) #the drawing speed
#
# #This is the head
# toka.penup()
# toka.goto(120,-50)
# toka.pendown()
# toka.circle(70)
#
# #this is the left ear
# toka.penup()
# toka.goto(50,30)
# toka.pendown()
# toka.goto(90,150)
#
# # #this is the left ear
# toka.goto(100,85)
#
# # #This is the right ear
# toka.penup()
# toka.goto(150,80)
# toka.pendown()
# toka.goto(150,150)
# toka.goto(180,55)
#
# #this is the left eye
# toka.penup()
# toka.goto(90,10)
# toka.pendown()
# toka.begin_fill()
# toka.color('light grey')
# toka.circle(20)
# toka.end_fill()
# #this is the right eye
# toka.penup()
# toka.goto(150,10)
# toka.pendown()
# toka.begin_fill()
# toka.color('light grey')
# toka.circle(20)
# toka.end_fill()
#
# #this is the mouth
# toka.penup()
# toka.goto(100,-10)
# toka.pendown()
# toka.color('black')
# toka.goto(140,-10)
#
# #this is the left body line
# toka.penup()
# toka.color('black')
# toka.goto(90,-40)
# toka.pendown()
# toka.goto(80,-120)
#
# #this is the bottom line
# toka.goto(150,-120)
#
# #this is the left body line
# toka.goto(150,-40)
#
# #this will draw its tail
# toka.penup()
# toka.goto(80,-120)

# turtle.exitonclick() #Keeps pycharm window open

import turtle
toka = turtle.Turtle()

toka.shape('turtle')
screen=turtle.Screen() #makes screen an object
screen.bgcolor('black')

toka.speed(20) #the drawing speed

toka.begin_fill()
toka.color('yellow')
toka.right(60)
toka.forward(200) # draw base
toka.right(120)
toka.forward(200)
toka.right(120)
toka.forward(200)
toka.done()
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
toka.goto(0,50)

turtle.exitonclick() #Keeps pycharm window open