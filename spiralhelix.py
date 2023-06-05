import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("black")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle.speed("fastest")
turtle_color = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(15):
    turtle_instance.color(turtle_color[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

turtle.mainloop()