import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
#t_turtle.shape("turtle")
#t_turtle.color('green')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# Generate a random walk
#def random_walk()

# Draw a square 
#for _ in range(4):
#    t_turtle.forward(100)
#    t_turtle.right(90)

# Draw a dashed line
#for _ in range(15):
#    t_turtle.forward(10)
#    t_turtle.pencolor("black")
#    t_turtle.forward(10)
#    t_turtle.pencolor("white")

# Draw a different shape
#def draw_shape(num_sides):
#    angle = 360 / num_sides
#    for _ in range(num_sides):
#        t_turtle.forward(100)
#        t_turtle.right(angle)


#for shape_size_n in range(3, 11):
#    t_turtle.color(random.choice(colours))
#    draw_shape(shape_size_n)
   




screen = Screen()
screen.exitonclick()

