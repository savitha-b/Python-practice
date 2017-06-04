import turtle

def draw_initials():
    window = turtle.Screen()
    window.bgcolor("yellow")
    sb = turtle.Turtle()
    sb.shape("turtle")
    sb.color("blue")
    sb.speed(10)
    sb.right(180)
#letter S
    for i in range(0,3):
        sb.forward(112)
        sb.left(90)
    sb.right(180)
    for i in range(0,2):
        sb.forward(112)
        sb.right(90)
    sb.right(90)
    sb.penup()
    sb.forward(200)
#letter B
    sb.pendown()
    for i in range(0,2):
        sb.forward(100)
        sb.left(90)
    sb.right(45)
    sb.forward(20)
    sb.left(45)
    sb.forward(90)
    sb.penup()
    sb.backward(90)
    sb.right(135)
    sb.pendown()
    sb.forward(20)
    sb.left(45)
    for i in range(0,2):
        sb.forward(100)
        sb.left(90)
    sb.forward(230)
    
    sb.hideturtle()
    window.exitonclick()

draw_initials()
