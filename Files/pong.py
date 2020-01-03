# Simply importing a package to work with graphics
import turtle

win = turtle.Screen()
win.title("Pong By darkdevilxy")
win.bgcolor("black")
win.setup(height=600, width=800)
win.tracer(0)  # Prevent the window from auto updating

# Score settings
scoreA = 0
scoreB = 0
scoreC = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.shape("square")
paddleA.color("white")
paddleA.penup()
paddleA.goto(-340, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.shape("square")
paddleB.color("white")
paddleB.penup()
paddleB.goto(340, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.08
ball.dy = -0.08

# Pen
pen = turtle.Turtle()
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {} : Single Player {}".format(scoreA, scoreB, scoreC), align="center",
          font=("Arial", 16, "normal"))


# Function

def paddleAUp():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleBUp():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keyboard Binding
win.listen()
win.onkeypress(paddleAUp, "w")
win.onkeypress(paddleAUp, "W")
win.onkeypress(paddleADown, "S")
win.onkeypress(paddleADown, "s")

win.onkeypress(paddleBUp, "Up")
win.onkeypress(paddleBDown, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -0.5

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -0.5

    if paddleB.ycor() > 247:
        paddleB.sety(247)
    if paddleB.ycor() < -243:
        paddleB.sety(-243)

    if paddleA.ycor() > 247:
        paddleA.sety(247)
    if paddleA.ycor() < -243:
        paddleA.sety(-243)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        ball.dx = 0.08
        ball.dy = -0.08
        pen.clear()
        pen.write("Player A: {}  Player B: {} : Single Player {}".format(scoreA, scoreB, scoreC), align="center",
                  font=("Arial", 16, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        ball.dx = 0.08
        ball.dy = -0.08
        pen.clear()
        pen.write("Player A: {}  Player B: {} : Single Player {}".format(scoreA, scoreB, scoreC), align="center",
                  font=("Arial", 16, "normal"))

    # Collision with paddle
    if (325 < ball.xcor()) and paddleB.ycor() + 48 > ball.ycor() > paddleB.ycor() - 48:
        ball.dx *= -1.1
        scoreC += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {} : Single Player {}".format(scoreA, scoreB, scoreC), align="center",
                  font=("Arial", 16, "normal"))

    elif ball.xcor() < -325 and paddleA.ycor() + 48 > ball.ycor() > paddleA.ycor() - 48:
        ball.dx *= -1.1
        scoreC += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {} : Single Player {}".format(scoreA, scoreB, scoreC), align="center",
                  font=("Arial", 16, "normal"))

    if ball.dx > 1.5:
        ball.dx = 1.2
    if ball.dy > 1.5:
        ball.dy = 1.2
