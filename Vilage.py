import turtle
from random import choice

# Helper function to generate random x-coordinate for a house
def get_random_x(size):
    return choice(range(-300, 300, size + 50))

# Helper function to generate random y-coordinate for a house
def get_random_y(size):
    return choice(range(-300, 300, size + 50))

# Helper function to draw a house
def draw_house(x, y, size, house_color, roof_color, door_color, window_color):
    Jim = turtle.Turtle()  # Create a turtle object
    Jim.shape('turtle')  # Set the shape of the turtle
    Jim.speed(1)  # Set the drawing speed

    # Draw the house
    Jim.penup()  # Lift the pen up
    Jim.goto(x, y)  # Move the turtle to the specified position
    Jim.color(house_color)  # Set the color for the house
    Jim.begin_fill()  # Begin filling the house with color
    for _ in range(4):
        Jim.forward(size)  # Move forward by the specified size
        Jim.right(90)  # Turn right by 90 degrees to form a square
    Jim.end_fill()  # End filling the house with color

    # Draw the roof
    Jim.penup()  # Lift the pen up
    Jim.goto(x, y)  # Move the turtle to the specified position
    Jim.pendown()  # Put the pen down
    Jim.color(roof_color)  # Set the color for the roof
    Jim.begin_fill()  # Begin filling the roof with color
    Jim.left(45)  # Rotate the turtle 45 degrees to the left for the roof angle
    for _ in range(2):
        Jim.forward(size * 0.707)  # Move forward by approximately sqrt(2)/2 times the size
        Jim.right(90)  # Turn right by 90 degrees to form a right angle
    Jim.end_fill()  # End filling the roof with color

    # Draw the door
    door_x = x + size * 0.65  # Calculate the x-coordinate of the door's position
    door_y = y - size * 0.5  # Calculate the y-coordinate of the door's position
    Jim.penup()  # Lift the pen up
    Jim.goto(door_x, door_y)  # Move the turtle to the door's position
    Jim.pendown()  # Put the pen down
    Jim.left(45)  # Set the orientation of the turtle for drawing the door
    Jim.fillcolor(door_color)  # Set the fill color for the door
    Jim.begin_fill()  # Begin filling the door with color
    for _ in range(2):
        Jim.forward(size * 0.5)  # Move forward by half of the specified size for door width
        Jim.left(90)  # Turn left by 90 degrees to form a rectangle
        Jim.forward(size * 0.3)  # Move forward by 30% of the specified size for door height
        Jim.left(90)  # Turn left by 90 degrees to complete the rectangle
    Jim.end_fill()  # End filling the door with color

    # Draw the window
    Jim.penup()  # Lift the pen up
    Jim.goto(x + size * 0.10, y)  # Calculate the position of the window
    Jim.pendown()  # Put the pen down
    Jim.fillcolor(window_color)  # Set the fill color for the window
    Jim.begin_fill()  # Begin filling the window with color
    for _ in range(4):
        Jim.forward(size * 0.25)  # Move forward by 25% of the specified size for window width and height
        Jim.left(90)  # Turn left by 90 degrees to form a square
    Jim.end_fill()  # End filling the window with color

# Helper function to draw grass
def draw_grass(x, y):
    t = turtle.Turtle()  # Create a turtle object
    t.pencolor('green')  # Set the pen color to green
    t.penup()  # Lift the pen up
    t.goto(x, y)  # Move the turtle to the specified position
    xp = 20  # Initial x-position for drawing grass
    t.pendown()  # Put the pen down
    t.left(15)  # Set the orientation of the turtle
    t.pensize(5)  # Set the pen size for drawing grass
    for _ in range(40):
        t.forward(20)  # Move forward by 20 units to draw a blade of grass
        t.penup()  # Lift the pen up
        t.goto(x + xp, y)  # Move the turtle to the next position for drawing grass
        t.pendown()  # Put the pen down
        xp += 20  # Increment the x-position for drawing grass

# Create a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown", "black", "gray"]

# Draw houses
for _ in range(20):
    draw_house(get_random_x(50), get_random_y(50), 50, choice(colors), choice(colors), choice(colors), choice(colors))

# Draw grass
draw_grass(0, 0)

# Keep the window open
turtle.done()
