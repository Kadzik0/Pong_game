"""
Pong game
"""

import turtle
import winsound

#screen declaration
wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

class Paddle(turtle.Turtle):

    def assign(self, speed=0, shape='square', color='white', shapesize=(5, 1), goto=(0, 0)):
        self.penup()
        self.speed(speed)
        self.shape(shape)
        self.color(color)
        self.shapesize(stretch_wid=shapesize[0], stretch_len=shapesize[1])
        self.goto(goto)

class Ball(Paddle):
    def __init__(self, dspeed=0.1):
        Paddle.__init__(self)
        self.dx=dspeed
        self.dy=dspeed

#score
score_a=0
score_b=0

#paddle A declaration
paddle_a=Paddle()
paddle_a.assign(0, 'square', 'white', (5,1), (-350,0))

# paddle_a = turtle.Turtle()
# paddle_a.speed(0)
# paddle_a.shape('square')
# paddle_a.color('white')
# paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# paddle_a.penup()
# paddle_a.goto(-350,0)

#paddle 2 declaration
paddle_b=Paddle()
paddle_b.assign(0, 'square', 'white', (5,1), (350,0))

# paddle_b = turtle.Turtle()
# paddle_b.speed(0)
# paddle_b.shape('square')
# paddle_b.color('white')
# paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# paddle_b.penup()
# paddle_b.goto(350,0)

#ball declaration
ball=Ball(0.15)
ball.assign(0, 'circle', 'blue', (1,1), (0,0))
# ball.dx=0.15
# ball.dy=0.15
# ball = turtle.Turtle()
# ball.speed(0)
# ball.shape('turtle')
# ball.color('white')
# ball.penup()
# ball.goto(0,0)
# ball.dx = .15
# ball.dy = .15

#pen declaration
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

#move paddle func
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

#move paddle func
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#move paddle func
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

#move paddle func
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_up, 'W')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_a_down, 'S')

wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

#Main game loop
while True:
    #print('.')
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        #ball.sety(290)
        ball.dy *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        #ball.sety(-290)
        ball.dy *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    #paddle check
    if ball.ycor()>paddle_b.ycor()-50 and ball.ycor()<paddle_b.ycor()+50 and ball.xcor() >= 340:
        ball.setx(340)
        ball.dx *=-1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor()>paddle_a.ycor()-50 and ball.ycor()<paddle_a.ycor()+50 and ball.xcor() <= -340:
        ball.setx(-340)
        ball.dx *=-1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)