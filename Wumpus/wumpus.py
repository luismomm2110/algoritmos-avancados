from solver import Solver
from world import World
from GUI import GUI


def main():
    world = World(2)
    solver = Solver(world)
    solver.print_path()
    for path in solver.find_paths():
        g = GUI(world, path)
        g.draw_grid()


if __name__ == "__main__":
    main()
