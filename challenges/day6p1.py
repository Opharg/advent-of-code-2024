# rough reimplementation from p2, because at some point I stopped working around p1 and just started overwriting
import get_input

def read_map():
    with open(r'./inputs/d6.txt', 'r') as file:
        return [list(line.strip()) for line in file.readlines()]


def find_start(map_grid):
    for i in range(len(map_grid)):
        for j in range(len(map_grid[0])):
            if map_grid[i][j] == '^':
                return i, j

    raise Exception('Guard not found')


def check_in_bounds(map_grid, position, target):
    if (0 <= position[0] + target[0] < len(map_grid)) and (0 <= position[1] + target[1] < len(map_grid[0])):
        return True
    return False


def check_for_obstacle(map_grid, position, target):
    if map_grid[position[0] + target[0]][position[1] + target[1]] == '#':
        return True
    return False


def turn(map_grid, position, facing):
    directions = [
        (-1, 0),  # n
        (0, 1),   # e
        (1, 0),   # s
        (0, -1)   # w
    ]
    for _ in range(4):
        if check_for_obstacle(map_grid, position, directions[facing]):
            facing = (facing + 1) % 4
        else:
            break
    return facing


def move(map_grid, position, target):
    map_grid[position[0]][position[1]] = 'X'
    return position[0] + target[0], position[1] + target[1]


def simulate_guard(map_grid, starting_position):
    # 0: north, 1: east, 2: south, 3: west
    facing = 0
    position = tuple(starting_position[:])

    directions = [
        (-1, 0),  # n
        (0, 1),   # e
        (1, 0),   # s
        (0, -1)   # w
    ]

    while True:
        if not check_in_bounds(map_grid, position, directions[facing]):
            return map_grid

        facing = turn(map_grid, position, facing)
        if not check_in_bounds(map_grid, position, directions[facing]):
            return map_grid

        new_position = move(map_grid, position, directions[facing])

        position = new_position


if __name__ == "__main__":
    #setup
    get_input.get_input(6)
    map_grid = read_map()
    starting_position = find_start(map_grid)

    steps = simulate_guard(map_grid, starting_position)
    combined = ''.join([''.join(x) for x in map_grid])

    # +1 because guard hasn't actually moved off the map yet, thus not placed an X
    print(combined.count('X') + 1)
