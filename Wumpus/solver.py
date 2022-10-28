from world import World
import networkx as nx


class Solver:
    def __init__(self, world: World):
        self.world = world

    def print_path(self):
        for path in self.find_paths():
            print(path)

    def find_paths(self):
        try:
            if nx.has_path(self.world.table, 0, self.world.gold_position):
                return nx.all_simple_paths(self.world.table, 0, self.world.gold_position)
        except:
            return "Sem solucao"

        return "Sem solucao"
