import turtle
import random

game_over_display = turtle.Turtle()
game_over_display.color("white")
game_over_display.penup()
game_over_display.goto(0, 0)
game_over_display.hideturtle()

# Set up screen
screen = turtle.Screen()
screen.title("Breakout Clone")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Draw the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Draw the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 100)
ball.dx = random.randint(-5,-1)
ball.dy = -5

# Draw the bricks
brick_colors = ["red", "orange", "yellow", "green", "blue"]
bricks = []
for i in range(30): # increase to 10 iterations for more bricks
    brick = turtle.Turtle()
    brick.shape("square")
    brick.color(brick_colors[i%5]) # use modulo to cycle through colors
    brick.shapesize(stretch_wid=1, stretch_len=4)
    brick.penup()
    x_pos = -260 + (i % 10) * 54 # calculate x position based on index
    y_pos = 200 - (i // 10) * 30 # calculate y position based on index
    brick.goto(x_pos, y_pos)
    bricks.append(brick)

# Set up the score
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.goto(-280, 260)
score_display.write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))

# Set up the lives
lives = 3
lives_display = turtle.Turtle()
lives_display.color("white")
lives_display.penup()
lives_display.goto(200, 260)
lives_display.write(f"Lives: {lives}", align="left", font=("Arial", 14, "normal"))

# Move the paddle
def move_left():
    x = paddle.xcor()
    if x > -240:
        x -= 20
        paddle.setx(x)

def move_right():
    x = paddle.xcor()
    if x < 240:
        x += 20
        paddle.setx(x)

# Set up keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for a collision with the walls
    if ball.xcor() > 260 or ball.xcor() < -260:
        ball.dx *= -1
    if ball.ycor() > 260:
        ball.dy *= -1

    # Check for a collision with the paddle
    if ball.ycor() < -240 and (paddle.xcor() - 50) < ball.xcor() < (paddle.xcor() + 50):
        ball.dy *= -1

    # Check for a collision with the bricks
    for brick in bricks:
        if ball.distance(brick) < 20:
            brick.goto(-1000, -1000)
            bricks.remove(brick)
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))
            ball.dy *= -1

    # Check for game over
    if ball.ycor() < -300:
        lives -= 1
        lives_display.clear()
        lives_display.write(f"Lives: {lives}", align="left", font=("Arial", 14, "normal"))
        ball.goto(0, 0)
        ball.dy *= -1

        # Check for game over
        if lives == 0:
            game_over_display.write("Game Over", align="center", font=("Arial", 24, "normal"))
            break

    # Decrease the ball speed if there are fewer bricks left
    if len(bricks) == 0:
        ball.dx *= 0.9
        ball.dy *= 0.9

    # Move the paddle
    def move_left():
        x = paddle.xcor()
        if x > -240:
            x -= 20
            paddle.setx(x)

    def move_right():
        x = paddle.xcor()
        if x < 240:
            x += 20
            paddle.setx(x)

    # Set up keyboard bindings
    screen.listen()
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")

    turtle.delay(1)

    turtle.update()
