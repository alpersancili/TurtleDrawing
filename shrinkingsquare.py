import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light green")
drawing_board.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSquare(size):
    turtle_instance.forward(size)
    turtle_instance.left(90)
    size = size - 5

shrinkingSquare(150)
shrinkingSquare(120)
shrinkingSquare(90)
shrinkingSquare(60)
shrinkingSquare(30)

turtle.done()