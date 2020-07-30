
import turtle

rad = int(input("\n Enter the radius : "))
pen = turtle.Pen()
pen.right(90)
pen.up()  #it will not show anything that will be drawn on the interface
pen.forward(50)
pen.down()
pen.color('red','blue')  #color(foreground,background)
pen.begin_fill()
pen.circle(rad)
pen.end_fill()  #fill the background color into your circle

turtle.exitonclick()
