from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(5)

def  move_backward():
    tim.back(5)

def turn_right():
    tim.right(5)

def turn_left():
    tim.left(5)

def reset():
    tim.reset()

screen.listen()

screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkey(key='c', fun=reset)


screen.exitonclick()