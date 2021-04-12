# offset - moves the pointer so it will not start from the center but from the bottom of the screen
OFFSET = -350
# the size ofone side of the square that blockes the regular polygon
BASE_LENGTH = 700
import turtle
import math


def main():
    sides = get_and_check_input()
    calculate_and_print(sides)
    input("press enter to exit")


def get_and_check_input():
    # get background color
    background_color = input("please enter the background color name or code: ")
    turtle.bgcolor(background_color)
    # get fill color
    fill_color = input("please enter the fill color name or code: ")
    turtle.fillcolor(fill_color)
    # get and check speed
    speed = input("please enter the Turtle's speed between 1 (slowest) to 10 (faster) or 0 (fastest): ")
    while (not (speed.isdigit()) or int(speed) < 0 or int(speed) > 10):
        print("invalid input. please enter the Turtle's speed between 1 (slowest) to 10 (faster) or 0 (fastest): ")
        speed = input()
    speed = int(speed)
    turtle.speed(speed)
    # get and check number of sides
    sides = input("please enter number of sides (number greater then 3): ")
    while (not (sides.isdigit()) or (int(sides) < 3)):
        print("error - invalid input. please enter number of sides (number greater then 3): ")
        sides = input()
    sides = int(sides)
    return sides


def calculate_and_print(sides):
    #calculate the angle - 180 - the internal angle (the angle that the turtle does is the external one)
    angle = 180 - ((1 - (2 / sides)) * 180)

    #calculate the length of the sides so the regular polygon will not go off screen
    #as the number of side increases I will decreese the length of the side
    side_length = BASE_LENGTH
    # the max_perimeter is the length of the perimeter of the circle blocked in the base square
    max_perimeter = BASE_LENGTH * math.pi
    #I make sure that the perimiter will not exceed the max perimiter
    while (sides * side_length > max_perimeter):
        side_length -= 1
    #draw
    turtle.penup()
    #the right location on the screen to not go off screen in the rught side or upper side
    turtle.goto(-(side_length / 2), OFFSET)
    turtle.pendown()
    turtle.begin_fill()
    for side in range(sides):
        turtle.forward(side_length)
        turtle.left(angle)
    turtle.end_fill()


main()
