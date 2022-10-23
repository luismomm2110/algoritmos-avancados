from copy import deepcopy
import random
import networkx as nx


class World:
    def __init__(self, dimension):
        self.dimension = dimension
        self.table = self._create_table(dimension)
        self.wumpus_position = self._put_wumpus()
        self.stinks = self._put_stink()
        self.holes_positions = self._put_holes()
        self.breezes = self._create_breezes()
        self.gold_position = self._create_gold_position()

    def _create_table(self, dimension):
        G = nx.Graph()

        G.nodes = [node for node in range((dimension*dimension))]

        for i in range(dimension*dimension):
            if ((i + 1) % dimension != 0):
                G.add_edge(i, i+1)

        for j in G.nodes:
            if j + dimension in G.nodes:
                G.add_edge(j, j+dimension)

        return G

    def _put_wumpus(self):
        wumpus_position = random.randint(1, len(self.table.nodes)-1)
        return wumpus_position

    def _put_stink(self):
        stinks = []

        stinks = self._create_tips(stinks, self.wumpus_position+1)
        stinks = self._create_tips(stinks, self.wumpus_position-1)
        stinks = self._create_tips(
            stinks, self.wumpus_position+self.dimension)
        stinks = self._create_tips(
            stinks, self.wumpus_position-self.dimension)

        return stinks

    def _put_holes(self):
        count_holes = self.dimension // 4 + 1

        free_spaces = deepcopy(self.table.nodes)

        free_spaces.remove(self.wumpus_position)

        holes = []

        for _ in range(count_holes):
            holes.append(random.choice(free_spaces))

        return holes

    def _create_breezes(self):
        breezes = []

        breezes = self._create_tips(breezes, self.wumpus_position+1)
        breezes = self._create_tips(breezes, self.wumpus_position-1)
        breezes = self._create_tips(
            breezes, self.wumpus_position+self.dimension)
        breezes = self._create_tips(
            breezes, self.wumpus_position-self.dimension)

        return breezes

    def _create_gold_position(self):
        free_spaces = deepcopy(self.table.nodes)

        free_spaces.remove(0)
        free_spaces.remove(self.wumpus_position)
        free_spaces = list(set(free_spaces).difference(self.holes_positions))

        return random.choice(free_spaces)

    def _create_tips(self, obstacle, position):
        if position in self.table.nodes:
            obstacle.append(position)

        return obstacle
