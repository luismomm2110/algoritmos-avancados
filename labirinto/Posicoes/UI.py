import turtle
from collections import deque
import sys
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(1300, 700)


class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


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


def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    # aqui troco para uma labirinto
    # os ifs tambem trocam
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "#":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == "." or character == "E":
                path.append((screen_x, screen_y))

            # saida
            if character == "E":
                green.color("purple")
                green.goto(screen_x, screen_y)
                end_x, end_y = screen_x, screen_y
                green.stamp()
                green.color("green")

            if character == "S":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def end_program():
    wn.exitonclick()
    sys.exit()


grid = [
    "#########",
    "S..#.#...",
    "#..#....#",
    "#....#..E",
    "#########",
]


def search(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        time.sleep(0)
        # pop next entry in the frontier queue an assign to x and y location
        x, y = frontier.popleft()

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x-24, y))

        # godown
        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        # goright
        if(x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x + 24, y))

        # goup
        if(x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            solution[cell] = x, y
            # blue.goto(cell)
            # blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x, y)
        green.stamp()


def back_route(x, y):
    global start_x, start_y, end_x, end_y
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]


maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

walls = []
path = []
visited = set()
frontier = deque()
solution = {}


setup_maze(grid)
search(start_x, start_y)
back_route(end_x, end_y)
wn.exitonclick()
