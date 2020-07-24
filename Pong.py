
import turtle, time, math, random

t = turtle.Turtle()
t2 = turtle.Turtle()
ball = turtle.Turtle()
st = turtle.Turtle()
score1 = turtle.Turtle()
score2 = turtle.Turtle()
bord = turtle.Turtle()
ts = t.getscreen()
t.shape("square")
t2.shape("square")
ball.shape("circle")
t.speed('fast')
t2.speed('fast')
ball.speed('fast')
score1.speed('fast')
score2.speed('fast')
st.speed('fast')
bord.speed('fast')
t.penup()
t2.penup()
ball.penup()
score1.penup()
score2.penup()
st.penup()
t.setx(-200)
t2.setx(200)
score1.goto(-150,150)
score2.goto(150,150)
st.ht()
st.goto(-5,50)
st.clear()

x = 0
y1 = 0
y2 = 0
#Set to the same intiger as 'spbal'
#Will reset ball speed to this number
ballsped = 4
#Speed of paddles
spd = 3
#speed of ball
spbal = 4
#max x & y that the ball and pattles can move
mx = 250
my = 150
#Scores per side
leftS = 0
rightS = 0
#a,b,c,d set for constent movement
a = 1
b = 0
c = 1
d = 0
#stop pads from moving ball anymore, used after ball passes a paddle a certain distance 
frez = 0
#Stops every moving part
stpAll = 0
#The winning score
maxS = 7

#Drawing border
bord.penup()
bord.goto(mx,my)
bord.pendown()
bord.goto(-mx,my)
bord.goto(-mx,-my)
bord.goto(mx,-my)
bord.goto(mx,my)
bord.ht()

#Setting scoreboard to 0 
score1.ht()
score2.ht()
score1.write(leftS, font=("Arial", 16))
score2.write(rightS, font=("Arial", 16))

def start():
  st.write("3", font=("Arial", 20))
  time.sleep(1)
  st.clear()
  st.write("2", font=("Arial", 20))
  time.sleep(1)
  st.clear()
  st.write("1", font=("Arial", 20))
  time.sleep(1)
  st.clear()
  st.write("Go", font=("Arial", 20))
  time.sleep(1)
  st.clear()
  push()


def push():
  global x, ballsped, spbal
  if stpAll == 0:
    ball.forward(spbal)
  border()
  ballborder()
  ballwin()

def up1():
  global y1, spd, a, b
  a = 1
  b = 0

def down1():
  global y1, spd, a, b
  a = 0
  b = 1
  
def up2():
  global y2, spd, c, d
  c = 1
  d = 0

def down2():
  global y2, spd, c, d
  c = 0
  d = 1
  
def pads():
  global y1, y2, spd, a, b, c, d, stpAll
  if a == 1 and b == 0 and stpAll == 0:
    y1 += spd
    t.sety(y1)
  if b == 1 and a == 0 and stpAll == 0:
    y1 -= spd
    t.sety(y1)
  if c == 1 and d == 0 and stpAll == 0:
    y2 += spd
    t2.sety(y2)
  if d == 1 and c == 0 and stpAll == 0:
    y2 -= spd
    t2.sety(y2)

def border():
  global my, mx, y1, y2, yball, ballsped
  #y border for paddles
  specy = my - 15
  #turtle 1
  if t.ycor() >= specy or t.ycor() <= -specy:
    if t.ycor() >= specy:
      y1 = specy
    if t.ycor() <= -specy:
      y1 = -specy
  #turtle 2
  if t2.ycor() >= specy or t2.ycor() <= -specy:
    if t2.ycor() >= specy:
      y2 = specy
    if t2.ycor() <= -specy:
      y2 = -specy

#Makes the ball stay in the border and bounce on paddles
def ballborder():
  global my, mx, y1, y2, yball, ballsped, frez, spbal, a, b, c, d
  #Ball heading changer
  ss = ball.heading() * -1
  #Ball flipping around
  if a == 1:
    septics = random.randrange(0, 35)
  if b == 1:
    septics = random.randrange(-35, 0) 
  if c == 1:
    septons = random.randrange(0, 35)
  if d == 1:
    septons = random.randrange(-35, 0)
  #Special specs of the ball... y-cords
  ballspecs = my - 12
  #The cor of the left paddle
  paddleftx = t.xcor() + 15
  paddlefty1 = t.ycor() + 15
  paddlefty2 = t.ycor() - 15
  #the cor of the right paddle
  paddrightx = t2.xcor() - 15
  paddrighty1 = t2.ycor() + 15
  paddrighty2 = t2.ycor() - 15
  #Increase the balls hitbox
  ballbottom = ball.ycor() - 6
  balltop = ball.ycor() + 6
  #ball
  if ball.ycor() >= ballspecs or ball.ycor() <= -ballspecs:
    ball.seth(ss)
  if ball.xcor() >= paddrightx:
    if ballbottom <= paddrighty1 and balltop >= paddrighty2 and ball.heading() <= 90:
      ball.seth(180 + septics)
      spbal += 1
  if ball.xcor() <= paddleftx:
    if ballbottom <= paddlefty1 and balltop >= paddlefty2 and ball.heading() >= 90:
      ball.seth(0 + septons)
      spbal += 1

#Checks if a player got a point
def ballwin():
  global my, mx, y1, y2, yball, ballsped, leftS, rightS, frez, spbal
  #The x cor of the ball
  ballspices = mx - 12
  balleyes = 200
  if ball.xcor() >= balleyes or ball.xcor() <= -balleyes:
    frez = 1  
  if ball.xcor() >= ballspices:
    leftS += 1
    score1.clear()
    score1.write(leftS, font=("Arial", 16))
    ball.seth(180)
    y1=0;y2=0
    t.sety(y1),t2.sety(y2)
    ball.goto(0,0)
    frez = 0
    spbal = ballsped
    start()
  if ball.xcor() <= -ballspices:
    rightS +=1
    score2.clear()
    score2.write(rightS, font=("Arial", 16))
    ball.seth(0)
    y1=0;y2=0
    t.sety(y1),t2.sety(y2)   
    ball.goto(0,0)
    frez = 0
    spbal = ballsped
    start()
  winchek()
    
def winchek():
  global leftS, rightS, stpAll, maxS
  st.goto(-20,50)
  if leftS >= maxS:
    stpAll = 1
    st.write("Left Wins", font=("Arial", 20))
  if rightS >= maxS:
    stopAll = 1
    st.write("Right Wins", font=("Arial", 20))


ts.onkey(start, "1")
ts.onkey(push, "space")
ts.onkey(up1, "w")
ts.onkey(down1, "s")
ts.onkey(up2, "Up")
ts.onkey(down2, "Down")


ts.listen()

#start()
while True:
  push()
  pads()