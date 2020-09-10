#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Luca Damian
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightblue")
panel.bgpic(image)

#=======Add your code here======
speed(10)
Turtle()
color('red')
pensize(10)
up()
left(90)
forward(130)
left(90)
forward(15)
left(90)
forward(20)
dot(10)
left(90)
forward(60)
left(90)
forward(13)
dot(10)
left(90)
forward(270)
color('green')
down()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
up()
left(180)
forward(15)
right(90)
forward(8)
left(180)
pensize(5)
down()
forward(116)
up()
right(90)
forward(20)
right(90)
down()
forward(116)
up()
goto(200,100)
fillcolor([0,255,255])
down()
begin_fill()
circle(30)
end_fill()
up()
forward(50)
down()
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)






