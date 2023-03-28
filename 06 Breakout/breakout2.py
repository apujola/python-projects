import turtle
import time
import random

# Set up the screen
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=600, height=600)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5

# Create the bricks
bricks = []
for i in range(-230, 270, 90):
    for j in range(150, 250, 25):
        colors = ["red", "blue", "yellow", "green"]
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(random.choice(colors))
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()
        brick.goto(i, j)
        bricks.append(brick)

# Set up the score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Move the paddle
def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)

# Set up the keyboard bindings
win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for a collision with the paddle
    if ball.ycor() < -240 and ball.ycor() > -250 and ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50:
        ball.dy *= -1

    # Check for a collision with the walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    # Check for a collision with the ceiling
    if ball.ycor() > 290:
        ball.dy *= -1

    # Check for a collision with the bricks
    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            ball.dy *= -1
            score += 10
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Check if the game is over
    if ball.ycor() < -300:
        score_pen.clear()
        score_pen.write("Game Over", align="center", font=("Courier", 24, "normal"))
        time.sleep(2)
        win.bye()