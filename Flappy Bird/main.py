import time
import turtle
import random

# --- Screen setup ---
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("blue")

# --- Player setup ---
player = turtle.Turtle()
player.ht()
player.left(94)
screen.addshape("flappy-bird2.png")
player.shape("flappy-bird2.png")
player.pu()
player.goto(-200, 0)
player.st()

# --- Cloud setup ---
cloud = turtle.Turtle()
cloud.speed(0)
cloud.left(90)
screen.addshape("cloud.png")
cloud.shape("cloud.png")

# random position for the cloud
x = 250
y = random.randint(60, 220)
cloud.pu()
cloud.goto(x, y)

# --- Score setup ---
score = 0

# --- Gravity ---
gravity = -0.3
player_gravity = 1

# cloud moves continuously
screen.tracer(0)

# --- Walls setup ---
top1 = turtle.Turtle()
top1.speed(0)
top1.pu()
screen.addshape("1wall.png")
top1.goto(150, 200)
top1.left(90)
top1.shape("1wall.png")

bottom1 = turtle.Turtle()
bottom1.speed(0)
bottom1.pu()
bottom1.goto(150, -250)
screen.addshape("bottom1.png")
bottom1.shape("bottom1.png")
bottom1.left(90)

top2 = turtle.Turtle()
top2.speed(0)
top2.pu()
top2.goto(400, 300)
top2.left(90)
top2.shape("1wall.png")

bottom2 = turtle.Turtle()
bottom2.speed(0)
bottom2.pu()
bottom2.goto(400, -150)
bottom2.left(90)
bottom2.shape("bottom1.png")

# --- Scoreboard ---
board = turtle.Turtle()
board.pu()
board.ht()
board.goto(200, 200)
board.color("white")
board.write(score, font=("arial", 50, "bold"), align="center")

# --- Controls ---
def up(x, y):
    # called when clicking the mouse
    global player_gravity
    player_gravity = 6

def go_up():
    # called when pressing the space bar
    global player_gravity
    player_gravity = 6

screen.listen()
screen.onkey(go_up, "space")
screen.onclick(up)

# --- Main game loop ---
while True:
    screen.update()

    # move the cloud
    x = cloud.xcor()
    cloud.setx(x - 1)
    if cloud.xcor() < -270:
        cloud.setx(300)
        y = random.randint(0, 200)
        cloud.sety(y)

    # apply gravity to the player
    player_gravity += gravity
    y = player.ycor()
    y += player_gravity
    player.sety(y)

    # check bottom boundary
    if player.ycor() < -250:
        break

    # --- Wall 1 movement and collision ---
    x = bottom1.xcor()
    bottom1.setx(x - 2)
    if bottom1.xcor() < -280:
        bottom1.setx(280)
    if -240 < bottom1.xcor() < -175:
        if player.distance(bottom1) < 160:
            break

    x = top1.xcor()
    top1.setx(x - 2)
    if top1.xcor() < -280:
        top1.setx(280)
    if -225 < top1.xcor() < -175:
        if player.distance(top1) < 160:
            break

    # --- Wall 2 movement and collision ---
    x = top2.xcor()
    top2.setx(x - 2)
    if -225 < top2.xcor() < -175:
        if player.distance(top2) < 160:
            break

    x = bottom2.xcor()
    bottom2.setx(x - 2)
    if -225 < bottom2.xcor() < -175:
        if player.distance(bottom2) < 160:
            break

    # --- Scoring ---
    if player.xcor() == top1.xcor() or player.xcor() == top2.xcor():
        score += 1
        board.clear()
        board.write(score, font=("arial", 50, "bold"), align="center")

# --- Game Over ---
over = turtle.Turtle()
over.ht()
over.write("GAME OVER", font=("impact", 50, "bold"), align="center")
screen.bgcolor("red")
screen.update()
