import turtle

# Constants
PLAYER_A_SCORE = 0
PLAYER_B_SCORE = 0
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_SPEED = 0
PADDLE_STRETCH_WID = 5
PADDLE_STRETCH_LEN = 1
PADDLE_MOVE_STEP = 90
BALL_MOVE_X = 3
BALL_MOVE_Y = 3

# Initialize Window
window = turtle.Screen()
window.title('Ping Pong')
window.bgcolor('black')
window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

# Initialize Paddles and Ball
# ... (Initialization code remains the same)

# Initialize Score Display
pen = turtle.Turtle()
pen.speed(PADDLE_SPEED)
pen.color('blue')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# Initialize Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('orange')
ball.penup()
ball.goto(5, 5)


def display_score():
    pen.clear()
    pen.write("Player A: {}  Player B: {}".format(PLAYER_A_SCORE, PLAYER_B_SCORE), align="center",
              font=('Arial', 24, 'normal'))


display_score()


# Paddle Movement Functions
# ... (Movement functions remain the same)

# Initialize Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(PADDLE_SPEED)
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=PADDLE_STRETCH_WID, stretch_len=PADDLE_STRETCH_LEN)
right_paddle.penup()
right_paddle.goto(350, 0)

# Initialize Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(PADDLE_SPEED)
left_paddle.shape('square')
left_paddle.color('white')
left_paddle.shapesize(stretch_wid=PADDLE_STRETCH_WID, stretch_len=PADDLE_STRETCH_LEN)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Keyboard Bindings
# ... (Keyboard bindings remain the same)

# Ball Movement and Collision Detection
def move_ball():
    global PLAYER_A_SCORE, PLAYER_B_SCORE, BALL_MOVE_X, BALL_MOVE_Y

    # Move the ball
    ball.setx(ball.xcor() + BALL_MOVE_X)
    ball.sety(ball.ycor() + BALL_MOVE_Y)

    # Border checking
    # Top and bottom
    if ball.ycor() > 290 or ball.ycor() < -290:
        BALL_MOVE_Y *= -1

    # Left and right
    if ball.xcor() > 390:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        BALL_MOVE_X *= -1
        PLAYER_A_SCORE += 1
        display_score()

    elif ball.xcor() < -390:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        BALL_MOVE_X *= -1
        PLAYER_B_SCORE += 1
        display_score()

    # Paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        BALL_MOVE_X *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        BALL_MOVE_X *= -1


# Paddle Movement Functions
# Functions to move the paddles up and down
def moveRightPadleUp():
    y = right_paddle.ycor()
    y = y+90
    right_paddle.sety(y)

def moveRightPadleDown():
    y = right_paddle.ycor()
    y = y-90
    right_paddle.sety(y)

def moveLeftPadleUp():
    y = left_paddle.ycor()
    y = y+90
    left_paddle.sety(y)

def moveLeftPadleDown():
    y = left_paddle.ycor()
    y = y-90
    left_paddle.sety(y)

# Main Game Loop

 # Keyboard Bindings
window.listen()

window.onkey(moveLeftPadleUp, 'w')
window.onkey(moveLeftPadleDown,'s')
window.onkey(moveRightPadleUp, 'Up')
window.onkey(moveRightPadleDown, 'Down')

while True:
    window.update()
    move_ball()

# Exit on Click
window.exitonclick()
