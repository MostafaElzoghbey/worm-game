from turtle import *
from random import *
from math import *

setup(1000, 1000)
title("My worm game")

speed(0)
rt(260)
begin_poly()
fillcolor("yellow")
begin_fill()
lt(30)
fd(30)
lt(90)
circle(30, 270)
lt(90)
fd(30)
end_fill()
end_poly()
hideturtle()
p = get_poly()
register_shape("tu2", p)
clearscreen()

bgcolor("black")

tu1 = Turtle()
tu1.hideturtle()
tu1.speed(1000)
tu1.penup()
tu1.goto(-450, 450)
tu1.pendown()
tu1.pencolor("white")
tu1.begin_fill()
tu1.fillcolor("white")
for i in range(4):
    tu1.fd(900)
    tu1.rt(90)
tu1.end_fill()


tu2 = Turtle()
tu2.penup()
tu2.speed(0)
tu2.shape("tu2")
tu2.fillcolor("yellow")


def right():
    tu2.setheading(0)


def Up():
    tu2.setheading(90)


def left():
    tu2.setheading(180)


def Down():
    tu2.setheading(270)


listen()
onkeypress(right, "Right")
onkeypress(left, "Left")
onkeypress(Up, "Up")
onkeypress(Down, "Down")

tu3 = Turtle("square")
tu3.up()
tu3.speed(0)


X2, Y2 = tu2.pos()
X3, Y3 = tu3.pos()

sc = Turtle()
sc.speed(0)
sc.shape("square")
sc.color("green")
sc.penup()
sc.hideturtle()
sc.goto(0, 400)
sc.write("score: 0 ", align="center", font=("ds-digital", 24, "normal"))

sc1 = Turtle()
sc1.speed(0)
sc1.shape("square")
sc1.color("red")
sc1.penup()
sc1.hideturtle()
sc1.goto(0, 100)

score = 0
n = 0

while 1 == 1:

    if -430 < X2 < 430 and -430 < Y2 < 430:
        tu2.fd(1 + n)
        X2, Y2 = tu2.pos()

        if abs(X2 - X3) < 30 and abs(Y2 - Y3) < 30:
            n += 1
            tu3.setpos(randint(-450, 450), randint(-450, 450))
            X3, Y3 = tu3.pos()
            sc.clear()
            sc.write(
                "Score: {}  ".format(score),
                align="center",
                font=("ds-digital", 24, "normal"),
            )
            score += 100

    else:
        sc.clear()
        tu3.hideturtle()
        sc1.write("Game Over ", align="center", font=("ds-digital", 29, "bold"))
        sc.goto(0, 0)
        sc.write(
            "Your Score: {}  ".format(score - 100),
            align="center",
            font=("ds-digital", 23, "normal"),
        )
        break


done()
