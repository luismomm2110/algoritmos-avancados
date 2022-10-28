from time import sleep
from world import World
from os import system


CHAR_SIZE = 10
FILLER = "#"*10
WUMPUS = " "*2 + "wumpus" + " "*2
STINK = " "*3 + "stink" + " "*2
HOLE = " "*3 + "hole" + " "*3
BREEZE = " "*2 + "breeze" + " "*2
VISITED = " "*CHAR_SIZE
GOLD = " "*3 + "GOLD" + " "*3


class GUI:
    def __init__(self, world: World, solution):
        self.world = world
        self.solution = solution
        self.grid = dict()

    def draw_grid(self):
        self._initial_grid()
        for position in self.solution:
            self._update(position)
            self._draw_step()

    def _draw_step(self):
        sleep(1)
        system('clear')
        for row in range(0, self.world.dimension):
            print(FILLER*(self.world.dimension))
            for column in range(0, self.world.dimension):
                print(self.grid[row, column], end='')
            print('\n' + FILLER*(self.world.dimension))

    def _initial_grid(self):
        for row in range(0, self.world.dimension):
            for column in range(0, self.world.dimension):
                self.grid[row, column] = FILLER
        self.grid[0, 0] = " "*CHAR_SIZE

    def _update(self, flatten_position):
        position = flatten_position // self.world.dimension, flatten_position % self.world.dimension

        if flatten_position == self.world.wumpus_position:
            self.grid[flatten_position] = WUMPUS
        elif flatten_position == self.world.gold_position:
            self.grid[position] = GOLD
        elif flatten_position in self.world.stinks:
            self.grid[position] = STINK
        elif flatten_position in self.world.holes_positions:
            self.grid[position] = HOLE
        elif flatten_position in self.world.breezes:
            self.grid[position] = BREEZE
        else:
            self.grid[position] = VISITED
