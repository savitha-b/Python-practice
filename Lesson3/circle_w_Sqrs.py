import turtle

def draw_square(sqr):
    for i in range(0,4):
        sqr.forward(100)
        sqr.right(90)

def draw_shape():
    window = turtle.Screen() #creating a background to draw
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(0,36):
        draw_square(brad)
        brad.right(10)
     
    window.exitonclick()

draw_shape()


   
    
