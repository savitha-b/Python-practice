import turtle

def draw_petal(tri):
    for i in range(0,3):
        tri.forward(100)
        tri.right(170)

def draw_shape():
    window = turtle.Screen() #creating a background to draw
    window.bgcolor("yellow")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    for i in range(0,9):
        draw_petal(brad)
        brad.right(10)
     
    window.exitonclick()

draw_shape()
