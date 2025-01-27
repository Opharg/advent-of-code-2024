from get_input import get_input
from functools import cache

@cache
def possible_steps(location, plant) -> set[tuple[int, int]] | None:

    valid_steps = set()

    # up
    if location[0] - 1 >= 0 and static_plot_map[location[0] - 1][location[1]] == plant:
        valid_steps.add((location[0] - 1, location[1]))
    # down
    if location[0] + 1 < len(static_plot_map) and static_plot_map[location[0] + 1][location[1]] == plant:
        valid_steps.add((location[0] + 1, location[1]))
    # right
    if location[1] + 1 < len(static_plot_map[0]) and static_plot_map[location[0]][location[1] + 1] == plant:
        valid_steps.add((location[0], location[1] + 1))
    # left
    if location[1] - 1 >= 0 and static_plot_map[location[0]][location[1] - 1] == plant:
        valid_steps.add((location[0], location[1] - 1))

    if len(valid_steps) > 0:
        return valid_steps
    return None


def wander_area(start_location) -> (int, int):
    global plot_map
    plant = memory[start_location[0]][start_location[1]]
    current_area = []
    perimeter_length = 0

    # idk why just putting start_location into current_area doesn't work properly, but here we are
    new_locations = possible_steps(start_location, plant)
    if not new_locations:  # solo perimeter
        return 1, 4, plant
    for new_location in new_locations:
        if new_location not in current_area:
            # We shouldn't run possible_steps() multiple times on the same tiles. Just let cache handle it.
            perimeter_length += 4 - len(possible_steps(new_location, plant))
            plot_map[new_location[0]][new_location[1]] = None
            current_area.append(new_location)

    # Just loop over everything over and over until we are sure every connected tile has been found.
    # Could fix with intermediate lists and/or c-style label, but it's 4am and it works.
    current_area_changed = True
    while current_area_changed:
        current_area_changed = False
        for num in range(0, len(current_area)):
            new_locations = possible_steps(current_area[num], plant)
            if not new_locations:
                continue

            for new_location in new_locations:
                if new_location not in current_area:
                    current_area_changed = True
                    perimeter_length += 4 - len(possible_steps(new_location, plant))
                    plot_map[new_location[0]][new_location[1]] = None
                    current_area.append(new_location)

    return len(current_area), perimeter_length, plant


def calculate_price(areas) -> int:
    price = 0
    for area in areas:
        price += area[0] * area[1]

    return price


if __name__ == '__main__':
    # input
    get_input(12)
    with open(r'./inputs/d12.txt', 'r') as file:
        memory = file.read()

    memory = memory.split('\n')
    static_plot_map = [list(x) for x in memory]
    plot_map = [list(x) for x in memory]

    width = len(memory[0])
    height = len(memory)

    areas = []
    for i in range(height):
        for j in range(width):
            if plot_map[i][j] is not None:
                areas.append(wander_area((i, j)))

    total_price = calculate_price(areas)
    print('Part 1:', total_price)


    # TODO; Part 2, get edges by side and combine those that share side, and coordinate; continuous on other coordinate.