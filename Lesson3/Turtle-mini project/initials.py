import turtle

def draw_initials():
  window = turtle.Screen()
  window.bgcolor("yellow")
  sb = turtle.Turtle()
  sb.shape("turtle")
  sb.color("blue")
  sb.speed(10)
  
sb.right(180)
for i in range(0,3):
  sb.forward(100)
  sb.left(90)
sb.right(180)
for i in range(0,2):
  sb.forward(100)
  sb.right(90) 
sb.right(90)
sb.penup()
sb.forward(200)
sb.pendown()
for i in range(0,1):
  sb.forward(100)
  sb.left(90)
sb.right(45)
sb.forward(20)
sb.left(45)
sb.forward(80)
sb.penup()
sb.backward(80)
sb.right(135)
sb.forward(20)
sb.left(45)
for i in range(0,1):
  sb.forward(100)
  sb.left(90)
sb.forward(200)
turtle.hideturtle()
window.exitonclick()

draw_initials()
