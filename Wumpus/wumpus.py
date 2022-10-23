from world import World


def main():
    world = World(3)
    table = world.table
    print(table.nodes)
    print(table.edges)
    print(world.wumpus_position)
    print(world.stinks)
    print(world.holes_positions)
    print(world.gold_position)


if __name__ == "__main__":
    main()
