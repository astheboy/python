from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotation_right():
    tim.right(10)


def rotation_left():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotation_right)
screen.onkey(key="a", fun=rotation_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()