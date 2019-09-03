'''
# Modify the starter code below to create your own cool drawing
# and then Pull Request it to your instructor.

# Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
# import turtle
# yoda=turtle.Turtle()
# screen=turtle.Screen() # makes a screen object
# screen.bgcolor('black') # colors the screen
# yoda.pensize(3) # width of pen line
# yoda.speed(10)  # speed of drawing. Go fast to not waste time.
# yoda.color("#00FF00")
# yoda.circle(100)  #head
# yoda.penup()
# yoda.setpos(50,185) #right ear
# yoda.pendown()
# yoda.goto(200,210)
# yoda.goto(88,145)
# yoda.penup()
# yoda.setpos(-50,185)  #left ear
# yoda.pendown()
# yoda.goto(-200,210)
# yoda.goto(-88,145)
# yoda.penup()
# yoda.setpos(200,-300)
# yoda.pendown()
# yoda.pencolor('#00FF00')
# yoda.write('Sign Your Name Here',font=("Arial", 12, "normal"))
#
# turtle.exitonclick() #Keeps pycharm window open

import turtle
toka = turtle.Turtle()
toka.shape('turtle')
screen=turtle.Screen() #makes screen an object
screen.bgcolor('tan')

toka.speed(10) #the drawing speed

#This is the head
toka.penup()
toka.goto(120,-50)
toka.pendown()
toka.circle(70)

#this is the left ear
toka.penup()
toka.goto(50,30)
toka.pendown()
toka.goto(90,150)

# #this is the left ear
toka.goto(100,80)

# #This is the right ear
toka.penup()
toka.goto(150,80)
toka.pendown()
toka.goto(150,150)
toka.goto(180,50)

#this is the left eye
toka.penup()
toka.goto(90,10)
toka.pendown()
toka.circle(20)

#this is the right eye
toka.penup()
toka.goto(150,10)
toka.pendown()
toka.circle(20)

#this is the mouth
toka.penup()
toka.goto(100,-10)
toka.pendown()
toka.goto(140,-10)

#this is the left body line
toka.penup()
toka.goto(90,-40)
toka.pendown()
toka.goto(80,-120)

#this is the bottom line
toka.goto(150,-120)

#this is the left body line
toka.goto(150,-40)

#this will draw its tail
toka.penup()
toka.goto(80,-120)

turtle.exitonclick() #Keeps pycharm window open