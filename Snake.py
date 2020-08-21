import turtle
import time
import random
import math

delay = 0.1
grid=math.floor(20/300)

boarder=turtle.Turtle()
boarder.speed(0)
boarder.penup()
boarder.goto(310,310)
boarder.pendown()
boarder.goto(-310,310)
boarder.goto(-310,-310)
boarder.goto(310,-310)
boarder.goto(310,310)
boarder.penup()
boarder.goto(1000,1000)

wn=turtle.Screen()
wn.title("Snake Game by PiKitty518")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,0)

segments = []

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

while True:
    wn.update()

    if head.distance(food) < 20:
        x=random.uniform(-14.5,14.5)
        y=random.uniform(-14.5,14.5)
        x=math.floor(x)
        y=math.floor(y)
        x*=20
        y*=20
        print(x,y)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    if head.xcor()>300 or head.xcor()<-300 or head.ycor()>300 or head.ycor()<-300:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        for segment in segments:
            segment.goto(1000,1000)
        x=random.uniform(-14.5,14.5)
        y=random.uniform(-14.5,14.5)
        x=math.floor(x)
        y=math.floor(y)
        x*=20
        y*=20
        print(x,y)
        food.goto(x,y)

        segments.clear()

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        if segments[index].distance(food) < 20:
            x=random.uniform(-14.5,14.5)
            y=random.uniform(-14.5,14.5)
            x=math.floor(x)
            y=math.floor(y)
            x*=20
            y*=20
            print(x,y)
            food.goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for segment in segments:
                segment.goto(1000,1000)
            x=random.randint(-grid,grid)*20
            y=random.randint(-grid,grid)*20
            round(x)
            round(y)
            print(x,y)
            food.goto(x,y)
            
            segments.clear()


    time.sleep(delay)


wn.mainloop()