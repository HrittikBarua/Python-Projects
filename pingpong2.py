import turtle as t
import time

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_SPEED = 100
WINNING_SCORE = 10

# Initialize Pygame
window = t.Screen()

window.title("Ping Pong")
window.bgcolor("Green")
window.setup(width=WIDTH, height=HEIGHT)
window.tracer(0)

# Create the paddles and ball
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("red")
left_paddle.shapesize(stretch_wid=7, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("blue")
right_paddle.shapesize(stretch_wid=7, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.20
ball.dy = -0.20





# Score variables
player_a_score = 0
player_b_score = 0

# Create score display
score_display = t.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Arial", 24, "normal"))

# Function to update the score display
def update_score():
    score_display.clear()
    score_display.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=("Arial", 24, "normal"))

# Function to move the left paddle up
def left_paddle_up():
    y = left_paddle.ycor()
    y += PADDLE_SPEED
    if y > HEIGHT / 2 - 50:
        y = HEIGHT / 2 - 50
    left_paddle.sety(y)

# Function to move the left paddle down
def left_paddle_down():
    y = left_paddle.ycor()
    y -= PADDLE_SPEED
    if y < -HEIGHT / 2 + 50:
        y = -HEIGHT / 2 + 50
    left_paddle.sety(y)

# Function to move the right paddle up
def right_paddle_up():
    y = right_paddle.ycor()
    y += PADDLE_SPEED
    if y > HEIGHT / 2 - 50:
        y = HEIGHT / 2 - 50
    right_paddle.sety(y)

# Function to move the right paddle down
def right_paddle_down():
    y = right_paddle.ycor()
    y -= PADDLE_SPEED
    if y < -HEIGHT / 2 + 50:
        y = -HEIGHT / 2 + 50
    right_paddle.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# Game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > HEIGHT / 2 - 10:
        ball.sety(HEIGHT / 2 - 10)
        ball.dy *= -1

    if ball.ycor() < -HEIGHT / 2 + 10:
        ball.sety(-HEIGHT / 2 + 10)
        ball.dy *= -1

    if ball.xcor() > WIDTH / 2:
        player_a_score += 1
        update_score()
        ball.goto(0, 0)
        
        ball.dx *= -1

    if ball.xcor() < -WIDTH / 2:
        player_b_score += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.color("blue")
        ball.setx(340)
        ball.dx *= -1

    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.color("red")
        ball.setx(-340)
        ball.dx *= -1

    # Check for a winning condition
    if  player_a_score >= WINNING_SCORE or player_b_score >= WINNING_SCORE:
        winner = "Player A" if player_a_score > player_b_score else "Player B"
        t.clear()  
        t.penup()
        t.goto(0, 0)
        t.color("white")
        t.write(f"{winner} wins!", align="center", font=("Arial", 36, "normal"))
        t.update()  
        time.sleep(4)
        window.bye()
