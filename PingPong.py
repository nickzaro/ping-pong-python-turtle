import turtle
import time
# ventana
ventana = turtle.Screen()
ventana.title("ping pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Juagador1
jugador1 = turtle.Turtle()
jugador1.speed(0)
jugador1.shape("square")
jugador1.color("white")
jugador1.penup()
jugador1.goto(-350, 0)
jugador1.shapesize(stretch_wid=5, stretch_len=1)

# Juagador2
jugador2 = turtle.Turtle()
jugador2.speed(0)
jugador2.shape("square")
jugador2.color("white")
jugador2.penup()
jugador2.goto(350, 0)
jugador2.shapesize(stretch_wid=5, stretch_len=1)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 2
pelota.dy = 2

# Red
red = turtle.Turtle()
red.color("white")
red.goto(0, 400)
red.goto(0, -400)


# teclas
# jugador1
def jugador1_up():
    jugador1.sety(jugador1.ycor()+10)


def jugador1_down():
    jugador1.sety(jugador1.ycor()-10)

# jugador2


def jugador2_up():
    jugador2.sety(jugador2.ycor()+10)


def jugador2_down():
    jugador2.sety(jugador2.ycor()-10)


ventana.listen()
ventana.onkeypress(jugador1_up, "w")
ventana.onkeypress(jugador1_down, "s")
ventana.onkeypress(jugador2_up, "Up")
ventana.onkeypress(jugador2_down, "Down")


while True:
    ventana.update()
    pelota.setx(pelota.xcor()+pelota.dx)
    pelota.sety(pelota.ycor()+pelota.dy)
    time.sleep(0.01)

    if pelota.ycor() > 290 or pelota.ycor() < -290:  # coliciones en y, rebota
        pelota.dy *= -1
    if pelota.xcor() > 390 or pelota.xcor() < -390:  # coliciones ne x, reaparece en el centro
        pelota.goto(0, 0)
        pelota.dx *= -1
    if (pelota.xcor() < -340 and pelota.xcor() > -350 #coliciones pelota-jugador1
            and (pelota.ycor() < jugador1.ycor() + 50) and (pelota.ycor() > jugador1.ycor()-50)):
        pelota.dx *= -1
    if (pelota.xcor() > 340 and pelota.xcor() < 350 #coliciones pelota-jugador2
            and (pelota.ycor() < jugador2.ycor() + 50) and (pelota.ycor() > jugador2.ycor()-50)):
        pelota.dx *= -1
