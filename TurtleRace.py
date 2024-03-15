import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("The ultimate turtle race.")
num_turtles = random.randint(2, 5)
colors = ["red", "green", "blue", "yellow", "purple"]
turtles = []
start = -200
gap = 0
line_drawer = turtle.Turtle()
line_drawer.penup()
line_drawer.goto(230, 200)  # Move to start position for the finish line
line_drawer.setheading(270)  # Point the turtle downwards

line_drawer.pendown()
line_drawer.forward(400)  # Draw the finish line
line_drawer.hideturtle()  # Optionally hide the line-drawing turtle

race_over = False

for i in range(num_turtles):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-300, start+gap)
    new_turtle.pendown()
    turtles.append(new_turtle)
    gap+=50


while not race_over:
    for racer in turtles:
        distance = random.randint(1, 10)
        racer.forward(distance)
        if racer.xcor() >= line_drawer.xcor():
            race_over = True
            winner = racer
            break


winner.penup()
winner.goto(0,0)
winner.pendown()
# Victory dance code here
winner.write(f"{winner.color()[0].capitalize()} Turtle Wins!", align="center", font=("Arial", 16, "normal"))

turtle.exitonclick()
