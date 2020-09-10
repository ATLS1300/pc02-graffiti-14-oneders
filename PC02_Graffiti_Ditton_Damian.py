'''
ATLS 1300
PC02 - Graffiti
Author (Starter Code): Dr. Z
Author (Student Code): Larry Ditton
May 29, 2020
8 Sep, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 500 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
up()

#kryptonite
goto(38,-67)
color("black", "chartreuse1")
down()
begin_fill()
goto(58,22)
goto(71,36)
goto(78,19)
goto(60,-69)
end_fill()
up()

goto(75,4)
down()
begin_fill()
goto(88,18)
goto(94,1)
goto(78,-72)
goto(60,-69)
end_fill()
up()

color("black")
goto(48,-68)
down()
goto(66,13)
goto(58,22)
up()
goto(66,13)
down()
goto(78,19)
up()

goto(70,-70)
down()
goto(83,-6)
goto(75, 4)
up()
goto(83,-6)
down()
goto(94,1)
up()

#monocle
color("gold1")
pensize(3)
goto(-20,92)
down()
circle(25)
up()
goto(-43,113)
down()
goto(-46,46)
up()
goto(-80,35)
down()
circle(64.5,33)
up()

#background snow
color("snow")
goto(-192,-247)
down()
begin_fill()
goto(-191,-229)
goto(-203,-223)
goto(-219,-202)
goto(-230,-173)
goto(-233,-148)
goto(-232,-130)
goto(-243,-112)
goto(-244,-89)
goto(-371,-89)
goto(-371,-247)
goto(-192,-247)
end_fill()
up()
goto(180,-247)
down()
begin_fill()
goto(177,-209)
goto(171,-199)
goto(164,-164)
goto(166,-152)
goto(165,-134)
goto(160,-126)
goto(157,-89)
goto(371,-89)
goto(371,-247)
goto(180,-247)
end_fill()
up()

#sun
goto(-371,247)
color("goldenrod1")
down()
dot(150)
up()
goto(-350,150)
right(90)
pensize(2)
down()
forward(100)
up()

goto(-300, 165)
left (10)
down()
forward(100)
up()

goto(-290, 200)
left(10)
down()
forward(100)
up()


#Text
goto(215,85)
down()
color("red")
style = ("Arial", 15, "normal")
write('"Superman Must DIE!"', font=style, align="center")
up()

goto(215,20)
down()
color("red")
style = ("Arial", 14, "normal")
write('"And I have Kryptonite!"', font=style, align="center")
up()
hideturtle()

exitonclick()