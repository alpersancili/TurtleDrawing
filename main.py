import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
num_sides = 6
angle = 360.0 / num_sides
size_lenght = 100

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(size_lenght)
turtle.done()