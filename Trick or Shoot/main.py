#######################################
# Import libraries

# Colors, movement, characters
import turtle
# Opening animation
import time
# Random positions for falling character
import random

#######################################
# Screen setup

# Create screen
# Note: "Screen" with capital S
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgcolor("purple")
screen.bgpic("fall-autumn-red-season (2).jpg")

# Countdown before game starts
anim = turtle.Turtle()
anim.color("white")
anim.penup()
anim.hideturtle()
for i in range(3, 0, -1):
    anim.write(i, font=("Broadway", 25, "bold"), align="center")
    time.sleep(1)
    anim.clear()

####################################
# Variables setup

# Player score
score = 0

#incrising speed
speed=1

# Score graphics
scorewrite = turtle.Turtle()
scorewrite.hideturtle()
scorewrite.color("white")
scorewrite.penup()
scorewrite.goto(160, 180)
scorewrite.write(score, font=("david", 30, "bold"))

# Lives (hearts)
heartlist = []
life = 3
for h in range(3):
    heart = turtle.Turtle()
    heart.up()
    heart.speed(0)
    screen.addshape("ChatGPT Image Jul 1, 2025, 03_33_12 PM (2).png")
    heart.shape("ChatGPT Image Jul 1, 2025, 03_33_12 PM (2).png")
    heart.left(90)
    heart.goto(h * 50 - 170, 180)
    heartlist.append(heart)

####################################
# Player (cat) setup

yora = turtle.Turtle()
yora.penup()
yora.hideturtle()
yora.left(90)
yora.goto(0, -160)
yora.showturtle()
screen.addshape("black-cat.png")
yora.shape("black-cat.png")

# Move right
def moveRight():
    # Get current position
    x = yora.xcor()
    # Move right on X axis
    yora.setx(x + 7)

# Move left
def moveLeft():
    # Get current position
    x = yora.xcor()
    # Move left on X axis
    yora.setx(x - 7)

# Keyboard bindings
screen.onkey(moveRight, "right")
screen.onkey(moveLeft, "left")
screen.listen()

####################################
# Projectile setup

til = turtle.Turtle()
til.hideturtle()
til.left(90)
til.penup()
screen.addshape("candy-corn.png")
til.shape("candy-corn.png")

# Explosion (bom)
bom = turtle.Turtle()
bom.hideturtle()
bom.left(90)
bom.penup()
bom.goto(0, 0)
screen.addshape("candy.png")
bom.shape("candy.png")

# Falling character
rock = turtle.Turtle()
rock.hideturtle()
rock.left(90)
rock.penup()
screen.addshape("witches1.png")
rock.shape("witches1.png")
rock.speed(speed)
tilisshow = "no"

# Shooting function
def shot():
    global score, tilisshow, life
    tilisshow = "no"
    # Hide projectile before firing
    til.hideturtle()
    til.speed(0)
    til.goto(yora)
    til.speed(5)
    til.showturtle()

    # Move projectile upward
    for x in range(20):
       global speed
       y = til.ycor()
       til.sety(y + 20)
       # Collision detection
       if til.distance(rock) < 25 and tilisshow == "no":
            tilisshow = "yes"
            bom.goto(x, y)
            bom.showturtle()
            print("+10 points")
            speed=speed+0.3
            rock.hideturtle()
            til.hideturtle()
            score = score + 10
            bom.hideturtle()
            scorewrite.clear()
            scorewrite.write(score, font=("david", 30, "bold"))

# Space key triggers shooting
screen.onkey(shot, "space")

####################################
# Game loop

while 2 < 5:
    tilisshow = "no"
    # Random X position for falling object
    x = random.randint(-170, 170)
    rock.hideturtle()
    rock.goto(x, 170)
    rock.speed(speed)
    rock.showturtle()

    # Falling motion
    for c in range(20):
        y = rock.ycor()
        rock.sety(y - 20)
        if rock.distance(yora) < 30 and tilisshow == "no":
            life = life - 1
            heartlist[life].ht()
            break
            """
            if life > 0:
                print "you have", life, "lifes left"
                rock.hideturtle()
                rock.speed(0)
                rock.showturtle()
            else:
                print "game over, your score is", score
            """

    

####################################
# Future ideas:
# Add a proper countdown or advanced missions
