import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("lightblue")
my_wn.title("spiral pattern on a canvas")
my_pen = turtle.Turtle()
size = 0
while True:
    my_pen.fd(size + 1)
    my_pen.left(90)
    size = size - 5
size = size + 1
turtle.done()