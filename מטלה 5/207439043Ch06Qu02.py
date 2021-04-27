# Ohad Ezer - 207439043
# Aviad Turm - 312556491

import turtle
turtle.bgcolor('cyan')
turtle.speed(0)
turtle.hideturtle()
OFFSET = 450
SQUARE_SIZE = 90


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
def create_square_array(board_size):
    for i in range(board_size):
        for j in range(board_size):
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
def color_board(board_size):
    for i in range(board_size):
        for j in range(board_size):
            if(i % 2 == 0 and j % 2 == 0):
                color_black(i + 1, j + 1)
            if (i % 2 != 0 and j % 2 != 0):
                color_black(i + 1, j + 1)
            if (i % 2 != 0 and j % 2 == 0):
                color_white(i + 1, j + 1)
            if (i % 2 == 0 and j % 2 != 0):
                color_white(i + 1, j + 1)


def get_board_size():
    print("please enter the size of the board(0-8) :")
    board_size = int(input())
    outfile = open('chesshistory.txt','a') # open file for votes numbers
    text_value = str(board_size) #convert int to str
    outfile.write(text_value + '\n') #write votes numbers in text file
    outfile.close()
    return board_size;

def get_and_print_history():
    infile = open('chesshistory.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)



def main():
    board_size = get_board_size()
    create_square_array(board_size)
    color_board(board_size)
    get_and_print_history()

main()

input("press enter to exit")

