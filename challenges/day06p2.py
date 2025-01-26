import multiprocessing
import tqdm
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


def check_for_obstacle(map_grid, position, target, ox, oy):
    if map_grid[position[0] + target[0]][position[1] + target[1]] == '#' \
            or (position[0] + target[0] == ox and position[1] + target[1] == oy):
        return True
    return False


def turn(map_grid, position, facing, ox, oy):
    directions = [
        (-1, 0),  # n
        (0, 1),   # e
        (1, 0),   # s
        (0, -1)   # w
    ]
    for _ in range(4):
        if check_for_obstacle(map_grid, position, directions[facing], ox, oy):
            facing = (facing + 1) % 4
        else:
            break
    return facing


def move(position, target):
    return position[0] + target[0], position[1] + target[1]


def simulate_guard(map_grid, starting_position, ox, oy):
    # 0: north, 1: east, 2: south, 3: west
    facing = 0
    position = tuple(starting_position[:])
    past_positions = set()
    past_positions.add((position, facing))

    directions = [
        (-1, 0),  # n
        (0, 1),   # e
        (1, 0),   # s
        (0, -1)   # w
    ]
    while True:
        if not check_in_bounds(map_grid, position, directions[facing]):
            return 0

        facing = turn(map_grid, position, facing, ox, oy)
        if not check_in_bounds(map_grid, position, directions[facing]):
            return 0

        new_position = move(position, directions[facing])

        if (new_position, facing) in past_positions:
            return ox, oy
        else:
            position = new_position
            past_positions.add((position, facing))


if __name__ == "__main__":

    #setup
    get_input.get_input(1)
    map_grid = read_map()
    starting_position = find_start(map_grid)

    # generate valid obstacle locations (might be faster to just check invalid ones too; ex. guard pos!)
    tasks = []
    for i in range(len(map_grid)):
        for j in range(len(map_grid[0])):
            if map_grid[i][j] != '#' and (i, j) != starting_position:
                tasks.append((map_grid, starting_position, i, j))

    # tqdm remnant from 40it/s
    with multiprocessing.Pool() as pool:
        results = pool.starmap(simulate_guard, tqdm.tqdm(list(tasks), total=len(tasks)))

    print(len([x for x in results if x != 0]))
