
import turtle
from random import choice

pen = turtle.Pen()
rad = 70
i = 1
colors = ['red','#123456','#C46855','#A47267']
while i<=5:
    c = choice(colors)
    pen.color('black',c)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    rad += 10
    i += 1

turtle.exitonclick()
