from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    tim.right(10)


def anti_clockwise():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=anti_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()
