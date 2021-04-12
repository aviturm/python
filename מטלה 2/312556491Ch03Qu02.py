#note - Idan Roth (PhD) authorised usage of functions that were not in class yet, such as lists
# Ohad Ezer - 207439043
# Aviad Turm - 312556491

import turtle
OFFSET = 500
BOARD_WIDTH = 7
BOARD_HIGHT = 6
RADIUS = 50
turtle.speed(0)
turtle.hideturtle()

#sub-function convert the grid number (1-8 col and 1-7 rows) to x,y coordinates
def convert(num):
    num = num * RADIUS * 2.35
    num -= OFFSET
    return num

#sub-function draw circle
def draw_circle(x,y):
    x = convert(x)
    y = convert(y)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(RADIUS)

#loop that draws all the empty circles
for i in range(BOARD_WIDTH):
    for j in range(BOARD_HIGHT):
        draw_circle(i+1,j+1)
turtle.speed(0)

#sub-function color a circle in red
def color_red(x,y):
    turtle.fillcolor('red')
    turtle.begin_fill()
    draw_circle(x,y)
    turtle.end_fill()
#sub-function color a circle in blue
def color_blue(x,y):
    turtle.fillcolor('blue')
    turtle.begin_fill()
    draw_circle(x,y)
    turtle.end_fill()


#demenstrating 10 first mooves
color_red(5,1)
color_blue(4,1)
color_red(4,2)
color_blue(3,1)
color_red(3,2)
color_blue(2,1)
color_red(1,1)
color_blue(5,2)
color_red(3,3)
color_blue(2,2)

#waits with the screen open untill the user presses enter
input("Click Enter when done")
