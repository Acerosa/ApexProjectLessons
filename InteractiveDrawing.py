import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("Interactive drawing.")
colours = ["red", "green", "blue", "yellow", "purple", "grey", "lightblue", "#FF7276", "lightgreen", "#F6BE00"]
elementsList = ['sky', 'sun', 'house', 'top', 'door', 'window', 'grass'] # For example, choose the first element 'sky'
phrase = "What Colour would you like the {} to be?\n 1 red, 2 green, 3 blue, 4 yellow, 5 purple, 6 grey, 7 light blue, 8 light red, 9 light green, 10 light yellow"
phrase2 = 'Choose {} colour'
chosenColour = turtle.textinput(phrase2.format(elementsList[0]), phrase.format(elementsList[0]))


screen.bgcolor(colours[int(chosenColour) - 1])
# sun
chosenColour = turtle.textinput(phrase2.format(elementsList[1]), phrase.format(elementsList[1]))
t.penup()
t.goto(150, 300)
t.pendown()
t.begin_fill()
for _ in range(12):
    t.color(colours[int(chosenColour) - 1])
    t.left(30)
    t.forward(30)
    t.right(60)
    t.forward(30)
t.end_fill()



# Draw the base of the house
chosenColour = turtle.textinput(phrase2.format(elementsList[2]), phrase.format(elementsList[2]))
t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor(colours[int(chosenColour) - 1])
t.fillcolor(colours[int(chosenColour) - 1])  # Set the fill color for the house
t.begin_fill()
for _ in range(4):
    t.forward(200)  # Base line
    t.right(90)
    # Left side
t.end_fill()

# Draw the roof
chosenColour = turtle.textinput(phrase2.format(elementsList[3]), phrase.format(elementsList[3]))
t.fillcolor(colours[int(chosenColour) - 1])  # Set the fill color for the roof
t.pencolor(colours[int(chosenColour) - 1])
t.begin_fill()
t.left(45)
for _ in range(2):
    t.forward(142)
    t.right(90)
t.end_fill()

# Position for the door
t.penup()
t.goto(80, -100)
t.pendown()
t.left(45)


# Draw the door
chosenColour = turtle.textinput(phrase2.format(elementsList[4]), phrase.format(elementsList[4]))
t.fillcolor(colours[int(chosenColour) - 1])  # Set the fill color for the door
t.pencolor(colours[int(chosenColour) - 1])
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# Draw door handle
t.pencolor('black')
t.penup()
t.goto(100, -150)
t.pendown()
t.dot(10)
#
#
# Position for the window
t.penup()
t.goto(10, 0)
t.pendown()

# Draw the window
chosenColour = turtle.textinput(phrase2.format(elementsList[5]), phrase.format(elementsList[5]))
t.fillcolor(colours[int(chosenColour) - 1])  # Set the fill color for the window
t.pencolor(colours[int(chosenColour) - 1])
t.begin_fill()
for _ in range(4):
    t.forward(50)  # Window width
    t.left(90)

t.end_fill()
#
# Draw the cross on the window
t.pencolor('black')
t.penup()
t.goto(35, 0)
t.pendown()
t.forward(50)
t.penup()
t.goto(10, -25)
t.pendown()
t.left(90)
t.forward(50)
t.left(90)  # Reset the turtle's direction to original

# grass
chosenColour = turtle.textinput(phrase2.format(elementsList[6]), phrase.format(elementsList[6]))
t.pencolor(colours[int(chosenColour) - 1])
t.penup()
t.goto(-350, -220)
xp = 20
t.pendown()
t.left(15)
t.pensize(5)
for _ in range(40):
    t.forward(20)
    t.penup()
    t.goto(-350 + xp, -220)
    t.pendown()
    xp +=20


turtle.exitonclick()
