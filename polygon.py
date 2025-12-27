import turtle
turtle.Screen().bgcolor("orange")

sc=turtle.Screen()
sc.setup(400,300)
turtle.title("polygon on a canvas")

board=turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.right(90)
    i+=1
turtle.done()