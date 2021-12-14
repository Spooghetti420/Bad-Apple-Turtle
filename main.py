import turtle
import re

def draw_pixel(x, y, width=16):
    turtle.penup()
    turtle.goto((x,y))
    turtle.begin_fill()
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()

def draw_row(size, color, height=16):
    turtle.fillcolor("black")
    pixels_left = size
    while pixels_left > 0:
        length = min(pixels_left,WIDTH-turtle.xcor())
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
        turtle.forward(length)
        pixels_left -= length
        turtle.end_fill()
        if turtle.xcor() >= WIDTH:
            turtle.setx(0)
            turtle.sety(turtle.ycor()-height)
            
WIDTH = 640
HEIGHT = 480
turtle.screensize(WIDTH, HEIGHT)
turtle.penup()
turtle.goto((-WIDTH, HEIGHT))
turtle.tracer(0)

frames = []
with open("data.txt") as data:
    frames = [line.strip() for line in data.readlines()]

for frame in frames[45:47]:
    i = 0
    pattern = r'(\d+)([BW])'
    spans = [m for m in re.finditer(pattern, frame)]
    for span in spans:
        if span.group(2) == "B":
            draw_row(int(span.group(1)), span.group(2))
    input()
