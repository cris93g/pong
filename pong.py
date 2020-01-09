import turtle
import winsound
windo = turtle.Screen()
windo.title("Pong")
windo.bgcolor("black")
windo.setup(width=800, height=600)
windo.tracer(0)


# score
score_a = 0
score_b = 0

# objects

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1


# score markup
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A:0  Player B:0", align="center",
          font=("Courier", 24, "normal"))


# function moving objs
def paddle_a_up():
    y = paddle_a.ycor()
    y += 15
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 15
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 15
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 15
    paddle_b.sety(y)


# keyboard bindings
windo.listen()
windo.onkeypress(paddle_a_up, "w")
windo.onkeypress(paddle_a_down, "s")
windo.onkeypress(paddle_b_up, "Up")
windo.onkeypress(paddle_b_down, "Down")

# game loop
while True:
    windo.update()

    # ball move
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # border checks
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player A:{}  Player B:{}" .format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A:{}  Player B:{}" .format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
    # paddle bounce
    if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350)and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
