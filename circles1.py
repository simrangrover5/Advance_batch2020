
import turtle
from random import choice

pen = turtle.Pen()
rad = 160
i = 1
colors = ['#123456','#C46855','#A47267']
while i<=5:
    c = choice(colors)
    pen.color('black',c)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.left(90)
    pen.up()
    pen.forward(20)
    pen.down()
    pen.right(90)
    rad -= 20
    i += 1

turtle.exitonclick()
