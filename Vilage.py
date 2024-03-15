import turtle

def draw_house(x, y, size, house_color, roof_color, door_color, window_color):
    Jim = turtle.Turtle()
    Jim.shape('turtle')
    Jim.speed(1)

    # Draw the house
    Jim.penup()
    Jim.goto(x, y)
    Jim.color(house_color)
    Jim.begin_fill()
    for _ in range(4):
        Jim.forward(size)
        Jim.right(90)
    Jim.end_fill()

    # Draw the roof
    Jim.penup()
    Jim.goto(x, y)
    Jim.pendown()
    Jim.color(roof_color)
    Jim.begin_fill()
    Jim.left(45)
    for _ in range(2):
        Jim.forward(size * 0.707)  # Approximate value for sqrt(2)/2 for the hypotenuse
        Jim.right(90)
    Jim.end_fill()

    # Draw the door
    door_x = x + size * 0.65
    door_y = y - size * 0.5  # Adjusted y-coordinate
    Jim.penup()
    Jim.goto(door_x, door_y)
    Jim.pendown()
    Jim.left(45)
    Jim.fillcolor(door_color)
    Jim.begin_fill()
    for _ in range(2):
        Jim.forward(size * 0.5)
        Jim.left(90)
        Jim.forward(size * 0.3)
        Jim.left(90)
    Jim.end_fill()

    # Draw the window
    Jim.penup()
    Jim.goto(x + size * 0.10, y)
    Jim.pendown()
    Jim.fillcolor(window_color)
    Jim.begin_fill()
    for _ in range(4):
        Jim.forward(size * 0.25)
        Jim.left(90)
    Jim.end_fill()

# Example usage:





draw_house(0,0,50, 'red', 'green', 'yellow', 'grey')
draw_house(60, 0, 50, 'orange', 'blue', 'pink', 'brown')
draw_house(60, -70, 50, 'blue', 'purple', 'grey', 'black')
draw_house(60, -200, 50, 'green', 'lightblue', 'lightred', 'white')


turtle.done()
