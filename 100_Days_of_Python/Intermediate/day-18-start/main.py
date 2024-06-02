from turtle import Turtle, Screen


t_turtle = Turtle()
t_turtle.shape("turtle")
t_turtle.color('green')

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
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t_turtle.forward(100)
        t_turtle.right(angle)


#for shape_size in range(3, 11):
#    draw_shape(shape_size)


screen = Screen()
screen.exitonclick()

