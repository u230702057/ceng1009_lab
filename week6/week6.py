import turtle
# -- setup --
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess =turtle.Turtle()
# -- functions --

def DrawPoly(turtle,side,size):
    angle= 360/side
    for i in range(side):
        turtle.forward(size)
        turtle.left(angle)
def DrawSpiral(turtle,angle):
    size = 1
    for i in range(100):
        turtle.forward(size)
        turtle.right(angle)
        size = size + 2
def DrawEquitriangle(turtle,size):
    DrawPoly(turtle,3,size)
def DrawStar(turtle,size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
def DrawSprite(turtle,legs,length):
    angle = 360/legs
    for i in range(legs):
        turtle.forward(length)
        turtle.backward(length)
        turtle.left(angle)

# # -- exercises --
# Exercise 1
# tess.color("hotpink")
# DrawPoly(tess,8,50)
# Exercise 2
# tess.color("blue")
# for i in range(20):
#     DrawPoly(tess, 4, 50)
#     tess.left(18)
# Exercise 3
# tess.pencolor("blue")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawSpiral(tess,90)
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess,89)
# Exercise 4
# DrawEquitriangle(tess,100)
# Exercise 5
# tess.color("hotpink")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# for i in range(5):
#     DrawStar(tess,100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()
# Exercise 6
DrawSprite(tess,15,120)
# -- finish --
wn.exitonclick()