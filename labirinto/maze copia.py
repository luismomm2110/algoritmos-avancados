#####################################
# Breadth First Search / Flood fill
# Davis MT
# 28.01.2018
#####################################

import turtle                    # import turtle library
import time
import sys
from collections import deque

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.title("A BFS Maze Solving Program")
# setup the dimensions of the working window
wn.setup(1300, 700)


# this is the class for the Maze
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

# this is the class for the finish line - green square in the maze


class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)


class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


grid = [
    "+++++++++++++++",
    "+s+       + +e+",
    "+ +++++ +++ + +",
    "+ + +       + +",
    "+ +   +++ + + +",
    "+ + + +   + + +",
    "+   + +   + + +",
    "+++++ +   + + +",
    "+     +   +   +",
    "+++++++++++++++",
]

# grid = [
# "+++++++++",
# "+ ++s++++",
# "+ ++ ++++",
# "+ ++ ++++",
# "+    ++++",
# "++++ ++++",
# "++++ ++++",
# "+      e+",
# "+++++++++",
# ]

# grid = [
# "+++++++++++++++",
# "+             +",
# "+             +",
# "+             +",
# "+     e       +",
# "+             +",
# "+             +",
# "+             +",
# "+ s           +",
# "+++++++++++++++",
# ]
grid_1 = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+s          +                 +               ++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++++e+++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
]

grid = [
    "#########",
    "S........",
    "#.......#",
    "# ...#..E",
    "#########",
]


def setup_maze(grid):                          # define a function called setup_maze
    # set up global variables for start and end locations
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            # assign the varaible "character" the the x and y location od the grid
            character = grid[y][x]
            # move to the x location on the screen staring at -588
            screen_x = -588 + (x * 24)
            # move to the y location of the screen starting at 288
            screen_y = 288 - (y * 24)

            if character == "#":
                # move pen to the x and y locaion and
                maze.goto(screen_x, screen_y)
                maze.stamp()                          # stamp a copy of the turtle on the screen
                # add coordinate to walls list
                walls.append((screen_x, screen_y))

            if character == "." or character == "E":
                # add " " and e to path list
                path.append((screen_x, screen_y))

            if character == "E":
                green.color("purple")
                # send green sprite to screen location
                green.goto(screen_x, screen_y)
                # assign end locations variables to end_x and end_y
                end_x, end_y = screen_x, screen_y
                green.stamp()
                green.color("green")

            if character == "S":
                # assign start locations variables to start_x and start_y
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()


def search(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        time.sleep(0)
        # pop next entry in the frontier queue an assign to x and y location
        x, y = frontier.popleft()

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            # backtracking routine [cell] is the previous cell. x, y is the current cell
            solution[cell] = x, y
            # blue.goto(cell)        # identify frontier cells
            # blue.stamp()
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x + 24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x, y)
        green.stamp()


def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
        # move the yellow sprite to the key value of solution ()
        yellow.goto(solution[x, y])
        yellow.stamp()
        # "key value" now becomes the new key
        x, y = solution[x, y]


# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}                           # solution dictionary


# main program starts here ####
setup_maze(grid)
search(start_x, start_y)
backRoute(end_x, end_y)
wn.exitonclick()
