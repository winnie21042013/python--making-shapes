import turtle
turtle.Screen().bgcolor("yellow")

sc=turtle.Screen()
sc.setup(400,300)
turtle.title("star pattern on a canvas")

board=turtle.Turtle()
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)

board.penup()
board.right(90)

board.backward(50)
board.right(90)
board.pendown()

board.backward(100)
board.right(120)
board.backward(100)
board.right(120)
board.backward(100)
board.right(120)
turtle.done()
