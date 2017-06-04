import turtle

def draw_square(sqr):
    for i in range(0,4):
        sqr.forward(100)
        sqr.right(90)

def draw_triangle(tri):
    for i in range(0,3):
        tri.backward(100)
        tri.left(120)

def draw_shape():
    window = turtle.Screen() #creating a background to draw
    window.bgcolor("red")
    pointer = turtle.Turtle()
    pointer.shape("turtle")
    pointer.color("yellow")
    pointer.speed(2)
    draw_square(pointer)
     
    cir = turtle.Turtle()
    cir.shape("circle")
    cir.color("green")
    cir.speed(2)
    cir.circle(100)


    nxt = turtle.Turtle()
    nxt.shape("arrow")
    nxt.color("white")
    nxt.speed(2)
    draw_triangle(nxt)
    window.exitonclick()

draw_shape()
