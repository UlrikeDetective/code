import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Clone")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    brick = turtle.Turtle()
    brick.shape("square")
    brick.color(colors[i])
    brick.penup()
    brick.goto(-240, 250 - i * 20)
    bricks.append(brick)

# Functions
def paddle_right():
    x = paddle.xcor()
    if x < 230:
        paddle.setx(x + 20)

def paddle_left():
    x = paddle.xcor()
    if x > -230:
        paddle.setx(x - 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle collision
    if (ball.dx > 0) and (ball.ycor() - 10 < paddle.ycor() < ball.ycor() + 10) and (
            paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if brick.distance(ball) < 20:
            brick.goto(1000, 1000)  # Move the brick off-screen
            ball.dy *= -1

    # Check for win
    win = True
    for brick in bricks:
        if brick.xcor() < 1000:
            win = False
            break
    if win:
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0
        print("You win!")
        break

    screen.update()

screen.mainloop()
