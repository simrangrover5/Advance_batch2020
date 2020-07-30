
import turtle

height = int(input("\n Enter the height : "))
pen = turtle.Pen()
i = 1
while i<=4:
    pen.forward(height)
    pen.left(90)
    i += 1
    
turtle.exitonclick()
