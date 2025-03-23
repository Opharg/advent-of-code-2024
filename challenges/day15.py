from enum import Enum

from get_input import get_input


class MapLegend(Enum):
    BOX = 'O'
    WALL = '#'
    FREE = '.'
    ROBOT = '@'


class Directions(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'


class Obstacle:

    def __init__(self, row: int, col: int, obstacle_type: MapLegend):
        self.position = (row, col)
        self.type = obstacle_type

    def __repr__(self):
        return f"{self.type}: {self.position}"


# globals, None to raise
map_elements: list[Obstacle] = None
warehouse_map: list[str] = None


def process_input(memory: str) -> str:
    global warehouse_map
    warehouse_map, instructions = memory.split('\n\n')  # no comment...
    warehouse_map = warehouse_map.split("\n")  # row, col

    instructions = instructions.replace('\n', '')

    return instructions


def create_obstacles() -> list[Obstacle]:
    global warehouse_map
    boxes = []
    for row in range(len(warehouse_map)):
        for col in range(len(warehouse_map[0])):
            if warehouse_map[row][col] != MapLegend.FREE.value:
                boxes.append(Obstacle(row, col, MapLegend(warehouse_map[row][col])))

    return boxes


def attempt_move(map_element: Obstacle, direction: Directions):
    # # debug
    # print(map_element, direction)
    # display_map()
    # input()

    global map_elements
    row, col = calculate_new_pos(map_element, direction)

    # find obstacles where the object wants to move and either tells the box to move, or doesn't move
    obs = next((e for e in map_elements if e.position == (row, col)), None)
    if obs:
        if obs.type == MapLegend.BOX:
            is_space_free = attempt_move(obs, direction)
            if not is_space_free:
                return False
        elif obs.type == MapLegend.WALL:
            return False

    # actually move and propagate up the stack, that the space is free now
    map_element.position = (row, col)
    return True


def calculate_new_pos(map_element: Obstacle, direction: Directions) -> tuple[int, int]:
    row, col = map_element.position

    match direction:
        case Directions.UP:
            row = row - 1
        case Directions.DOWN:
            row = row + 1
        case Directions.LEFT:
            col = col - 1
        case Directions.RIGHT:
            col = col + 1
        case _:
            raise ValueError("Invalid Direction")

    return row, col


def calculate_score() -> int:
    global map_elements

    score = 0
    for e in map_elements:
        if e.type != MapLegend.BOX:
            continue
        score = score + (100 * e.position[0] + e.position[1])
    return score


def debug_display_map():
    global map_elements
    global warehouse_map

    # clear map
    new_map = [
        list(x.replace(MapLegend.BOX.value, MapLegend.FREE.value)
             .replace(MapLegend.ROBOT.value, MapLegend.FREE.value))
        for x in warehouse_map]

    # redraw map
    for e in map_elements:
        if e.type == MapLegend.BOX or e.type == MapLegend.ROBOT:
            new_map[e.position[0]][e.position[1]] = e.type.value
    new_map = [''.join(x) for x in new_map]

    for e in new_map:
        print(e)
    print('\n')


def main():
    # input
    get_input(15)
    with open(r'./inputs/d15.txt', 'r') as file:
        memory = file.read()

    global warehouse_map
    global map_elements
    instructions = process_input(memory)
    map_elements = create_obstacles()

    # find robot
    robot = next((e for e in map_elements if e.type == MapLegend.ROBOT), None)
    assert robot

    for instruction in instructions:
        attempt_move(robot, Directions(instruction))

    print(f"Part 1: {calculate_score()}")

    # Part 2 should be relatively easy(tm) with the recursive propagation.
    # Just need to branch to the other half of the box when pushing up/down and only move if both branches can move
    # additional field for 2nd half of box in Obstacle?


if __name__ == '__main__':
    main()
