import turtle as trtl
import random

bob = trtl.Turtle()

bob.speed(0)

bob.ht()
bob.pensize(3)

player = trtl.Turtle()
count = 0
distance = 40
wall_width = 20
door_width = 20

def draw_Door():
    bob.penup()
    bob.forward(door_width)
    bob.pendown() 

def draw_Wall():
    bob.left(90)
    bob.forward(wall_width*2)
    bob.backward(wall_width*2)
    bob.right(90)
    

while (count < 26):
    if count > 4:
        door = random.randint(door_width, distance - 2*door_width)
        wall = random.randint(2*wall_width,distance - 2*door_width)
        if door < wall:
            bob.forward(door)
            draw_Door()
            bob.forward(wall - door - door_width)
            draw_Wall()
            bob.forward(distance - wall)
        else:
            bob.forward(wall)
            draw_Wall()
            bob.forward(door - wall)
            draw_Door()
            bob.forward(distance - door - door_width)
    bob.left(90)
    distance += wall_width
    count = (count + 1)

wn = trtl.Screen()

player.pencolor("blue")

def Up():
    player.setheading(90)
    player.forward(10)


def Down():
    player.setheading(270)
    player.forward(10)


def Left():
    player.setheading(180)
    player.forward(10)


def Right():
    player.setheading(0)
    player.forward(10)

wn.onkeypress(Up, "Up")
wn.onkeypress(Down, "Down")
wn.onkeypress(Left, "Left")
wn.onkeypress(Right, "Right")
wn.listen()

    
wn.mainloop()