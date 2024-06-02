from turtle import Turtle, Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color('green')

#for _ in range(4):
#    timmy_the_turtle.forward(100)
#    timmy_the_turtle.right(90)

for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pencolor("black")
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pencolor("white")



screen = Screen()
screen.exitonclick()

