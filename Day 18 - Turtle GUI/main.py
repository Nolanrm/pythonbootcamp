import turtle as t
import random as rand

my_turtle = t.Turtle()
t.colormode(255)
my_turtle.hideturtle()
my_turtle.pensize(10)
my_turtle.speed(0)
 
def rand_color():
    r = rand.randint(0,255)
    b = rand.randint(0,255)
    g = rand.randint(0,255)
    return (r,b,g)

def rand_angle_distance():
    return [rand.randint(0,360),rand.randint(10,40)]

def draw_shape(sides,color):
    my_turtle.color(color)
    angle = 360/sides
    for i in range(sides):
        my_turtle.forward(30)
        my_turtle.right(angle)

def rand_walk(paces):
    for _ in range(paces):
        walk = rand_angle_distance()
        my_turtle.color(rand_color())
        my_turtle.right(walk[0])
        my_turtle.forward(walk[1])

def draw_spirograph(size):
    my_turtle.pensize(1)
    for _ in range(int(360/size)):
        my_turtle.color(rand_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size)
        

#draw_spirograph(5)

#rand_walk(rand.randint(20,40))



x = -200
y = 200

while x <= 200:
    while y >= -200:
        my_turtle.color(rand_color())
        my_turtle.penup()
        my_turtle.goto(x,y)
        my_turtle.pendown()
        my_turtle.forward(1)
        y -= 20
    x += 20
    y = 200

# for i in range(5):
#     sides = i + 3
#     draw_shape(sides,rand_color())

screen = t.Screen()
screen.exitonclick()