#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Luca Damian
May 29, 2020
A creative art piece on a picture of Jeff Bezos. Intended to give Jeff Bezos red eye and create a variety of dollar signs ($) in different sizes and colors around his head.
'''

from turtle import
import random 

colormode(255)

# Create a panel to draw on
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h)

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightblue")
panel.bgpic(image)
speed(10)
Turtle()
color('red')
pensize(10)

#Add red eyes to Jeff Bezos 
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

#Thi$ is where we make the money 
repeats = range(15) 
for element in repeats: #this for loop will create 15 differently colored dollar signs in random locations on the panel 
    colors = [(155, 235, 134) , (56, 189, 21) , (58, 233, 12) , (31, 119, 8)]#four shades of green 
    color(random.choice(colors)) #chooses a random color from my selected list of shades of green above
    penup()
    pensize(10)
    goto(random.randint(-350,350),random.randint(-350,350))#chooses a random place on the panel to begin drawing the dollar sign 
    down()
    forward(50)#next 10 lines of code make the initial dollar sign shape 
    left(90)
    forward(50)
    left(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    penup() #next 14 lines of codes make two lines for the dollar signs 
    pensize(5)
    left(180)
    forward(15)
    right(90)
    forward(8)
    left(180)
    down()
    forward(116)
    up() 
    right(90)
    forward(20)
    right(90)
    down()
    forward(116)
    
    done()







