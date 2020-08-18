ans= int(input ("How many sides do you want in your shape. Please choose between three and ten:"))
import turtle
eric=turtle.Turtle()
eric.color('dark green')
angle = 360/ans
for i in range(ans):
    eric.forward(100)
    eric.left(angle)
turtle.done