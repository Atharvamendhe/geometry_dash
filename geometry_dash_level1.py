import turtle
import time

# ------------------ Screen ------------------
win = turtle.Screen()
win.title("Geometry Dash - Level 1 (Turtle)")
win.bgcolor("black")
win.setup(width=900, height=400)
win.tracer(0)

# ------------------ Player ------------------
player = turtle.Turtle()
player.shape("square")
player.color("cyan")
player.penup()

# ------------------ Ground ------------------
ground = turtle.Turtle()
ground.shape("square")
ground.color("white")
ground.penup()
ground.goto(0, -160)
ground.shapesize(stretch_wid=1, stretch_len=50)

# ------------------ Level Data ------------------
level_positions = [200, 350, 500, 700, 900, 1100, 1300]
obstacles = []

# ------------------ Physics ------------------
GRAVITY = -1.5
JUMP = 16
SCROLL_SPEED = 6

# ------------------ Game State ------------------
game_over = False
win_level = False

# ------------------ Functions ------------------
def create_level():
    obstacles.clear()
    for x in level_positions:
        spike = turtle.Turtle()
        spike.shape("square")
        spike.color("red")
        spike.penup()
        spike.goto(x, -130)
        spike.shapesize(stretch_wid=2, stretch_len=1)
        obstacles.append(spike)

def reset_game():
    global game_over, win_level
    game_over = False
    win_level = False

    player.goto(-350, -120)
    player.dy = 0

    for obs in obstacles:
        obs.hideturtle()
    create_level()

def jump():
    if player.ycor() <= -120 and not game_over and not win_level:
        player.dy = JUMP

def restart():
    reset_game()

# ------------------ Controls ------------------
win.listen()
win.onkeypress(jump, "space")
win.onkeypress(restart, "r")

# ------------------ Init ------------------
reset_game()

# ------------------ Game Loop ------------------
message = turtle.Turtle()
message.hideturtle()
message.color("white")

while True:
    win.update()
    time.sleep(0.02)

    if not game_over and not win_level:
        # Gravity
        player.dy += GRAVITY
        player.sety(player.ycor() + player.dy)

        if player.ycor() < -120:
            player.sety(-120)
            player.dy = 0

        # Scroll obstacles
        for obs in obstacles:
            obs.setx(obs.xcor() - SCROLL_SPEED)

            # Collision
            if (abs(player.xcor() - obs.xcor()) < 20 and
                abs(player.ycor() - obs.ycor()) < 40):
                game_over = True
                message.clear()
                message.write("GAME OVER\nPress R to Restart",
                              align="center",
                              font=("Arial", 20, "bold"))

        # Win condition
        if obstacles[-1].xcor() < -400:
            win_level = True
            message.clear()
            message.write("LEVEL COMPLETE!\nPress R to Restart",
                          align="center",
                          font=("Arial", 20, "bold"))

win.mainloop()
