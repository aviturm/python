# Ohad Ezer - 207439043
# Aviad Turm - 312556491

import turtle
turtle.bgcolor('cyan')
turtle.speed(0)
turtle.hideturtle()
OFFSET = 450
SQUARE_SIZE = 90
BOARD_SIZE = 8

#convert grid to coordinates
def convert(number):
    return (number * SQUARE_SIZE) - OFFSET
#create a square
def square(x,y):
    x = convert(x)
    y = convert(y)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    for corner_counter in range (4):
        turtle.forward(SQUARE_SIZE)
        turtle.left(90)

#loop create square array
def create_square_array():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            square(i + 1, j + 1)

#color square black
def color_black(x,y):
    turtle.fillcolor('brown')
    turtle.begin_fill()
    square(x,y)
    turtle.end_fill()
#color square white
def color_white(x,y):
    turtle.fillcolor('white')
    turtle.begin_fill()
    square(x,y)
    turtle.end_fill()
#loop color the board
def color_board():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if(i % 2 == 0 and j % 2 == 0):
                color_black(i + 1, j + 1)
            if (i % 2 != 0 and j % 2 != 0):
                color_black(i + 1, j + 1)
            if (i % 2 != 0 and j % 2 == 0):
                color_white(i + 1, j + 1)
            if (i % 2 == 0 and j % 2 != 0):
                color_white(i + 1, j + 1)

def main():
    create_square_array()
    color_board()

main()

input("press enter to exit")
