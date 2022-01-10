*********************************************************************
#You can use source codes as you want
#But You have to give our profile link in your code as comment
#Copy Below Codes and Paste in your codes Comment Section
*********************************************************************
#Github: https://github.com/vipinjangra
#Youtube: https://www.youtube.com/c/vipincoding/
#Blog: http://vipincoding.wordpress.com/
#Website: http://vipincoding.blogspot.com
#Facebook: https://www.facebook.com/vipincoding
#Instagram: https://www.instagram.com/vipincoding/
*********************************************************************

####Youtube

import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("vipin coding")

v = turtle.Turtle()
v.pencolor("white")
v.speed(0)
v.width(3)
v.fillcolor("red")
v.hideturtle()

# position of design
v.penup()
v.goto(-10, 120)
v.pendown()

#youtube box code
def curve1():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve2():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve3():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve4():
    for i in range(30):
        v.right(3)
        v.forward(2)

v.pencolor("#FF0000")
v.begin_fill()
v.forward(100)
curve1()
v.forward(50)
curve2()
v.forward(100)
curve3()
v.forward(50)
curve4()
v.forward(30)
v.end_fill()

v.penup()
v.right(90)
v.forward(30)
v.pendown()


#triangle code
v.fillcolor("white")
v.begin_fill()
v.pencolor("white")
v.pensize(5)
v.forward(60)
v.left(120)
v.forward(60)
v.left(120)
v.forward(60)
v.end_fill()

turtle.done()




###instagram

import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("vipin coding")

v = turtle.Turtle()
v.pencolor("white")
v.speed(0)
v.width(8)
v.hideturtle()

# position of design
v.penup()
v.goto(-10, 120)
v.pendown()

def curve1():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve2():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve3():
    for i in range(30):
        v.right(3)
        v.forward(2)

def curve4():
    for i in range(30):
        v.right(3)
        v.forward(2)

v.forward(80)
curve1()
v.forward(80)
curve2()
v.forward(80)
curve3()
v.forward(80)
curve4()
v.forward(15)

v.penup()
v.right(90)
v.forward(78)
v.pendown()
v.pensize(8)
v.circle(25)

v.penup()
v.left(90)
v.forward(60)
v.left(90)
v.forward(40)
v.pendown()
v.dot(14)

turtle.done()




####Windows logo

import turtle

window = turtle.Screen()
window.bgcolor("#00adef")
window.title("vipin coding")

v = turtle.Turtle()
v.pencolor("black")
v.speed(1)
v.width(1)
v.hideturtle()

#position of design
v.color('white')
v.goto(-50,60)
v.begin_fill()
v.goto(100, 100)
v.goto(100, -100)
v.goto(-50, -60)

v.goto(-50, 60)
v.end_fill()

v.color("#00adef")
v.goto(15, 100)
v.color("#00adef")
v.width(12)
v.goto(15, -80)
v.penup()

v.goto(100, 0)
v.pendown()
v.goto(-100, 0)

turtle.done()




###Target Logo

import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("vipin coding")

v = turtle.Turtle()
v.pencolor("red")
v.speed(1)
v.width(1)
v.hideturtle()

#position of design
v.penup()
v.goto(0, 0)
v.pendown()

#outer Circle
v.dot(500,"#E80018")

v.penup()
v.goto(0,0)
v.pendown()

#inner circle
v.dot(350,"white")

v.penup()
v.goto(0,0)
v.pendown()

#center circle
v.dot(200,"#E80018")
turtle.done()
