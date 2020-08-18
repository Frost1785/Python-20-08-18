import turtle
import time

eric = turtle.Turtle()
canvas = turtle.Screen()
canvas.bgcolor('pink')
eric.color('red')
eric.shape('turtle')
eric.speed(50)

eric.pencolor('red')
eric.pensize(25)
eric.forward(100)
time.sleep(2)
eric.left(90)
eric.forward(100)
time.sleep(1.5)
eric.left(90)
eric.forward(100)
time.sleep(1.5)
eric.left(90)
eric.forward(100)
time.sleep(2)
eric.left(90)
eric.forward(100)
eric.write("Hello")



turtle.done