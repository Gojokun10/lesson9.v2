import turtle



draw = turtle.Turtle()

#num_side = 20
#side_lenght = 60
#angle = 360.0 / num_side

#for i in range(num_side):
    #draw.forward(side_lenght)
    #draw.right(angle)



window = turtle.Screen()
window.bgcolor("grey")
window.title("My window for turtle")
draw.color('yellow')

#def shapefunction(size, sides):
    #for i in range(sides):
        #draw.fd(size)
        #draw.left(360.0 / sides)
        #size = size + 5

#shapefunction(150,4)
#shapefunction(170,4)
#shapefunction(190,4)
#shapefunction(210,4)
#shapefunction(230,4)


window2 = turtle.Screen()
pen = turtle.Pen()
pen.penup()
pen.goto(-220, 50)
pen.pendown()

def drawV():
    pen.right(60)
    pen.forward(40)
    pen.left(120)
    pen.forward(40)
    pen.penup()
drawV()

def drawL():
    pen.right(60)
    pen.forward(20)
    pen.pendown()
    pen.right(90)
    pen.forward(35)
    pen.left(90)
    pen.forward(20)
    pen.penup()


drawL()

def drawA():
    pen.forward(20)
    pen.left(60)
    pen.pendown()
    pen.forward(40)
    pen.right(120)
    pen.forward(40)
    pen.left(180)
    pen.forward(20)
    pen.left(60)
    pen.forward(20)
    pen.penup()

drawA()

def drawD():
    pen.right(180)
    pen.forward(20)
    pen.right(60)
    pen.forward(20)
    pen.left(60)
    pen.forward(20)
    pen.pendown()
    pen.left(90)
    pen.forward(37)
    pen.right(90)
    pen.forward(15)
    pen.right(30)
    pen.forward(17.5)
    pen.right(60)
    pen.forward(23)
    pen.right(60)
    pen.forward(17.5)
    pen.right(30)
    pen.forward(15)
drawD()

turtle.done()
turtle.exitonclick()