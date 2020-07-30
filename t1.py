
import turtle

height = int(input("\n Enter the height : "))
width = int(input("\n Enter the width : "))
pen = turtle.Pen()
i = 1
while i<=4:
    if i%2 == 0:
        pen.forward(width)
    else:
        pen.forward(height)
    pen.left(90)
    i += 1
    
turtle.exitonclick()
