from get_input import get_input


def find_trailheads(topographic_map) -> list[tuple]:
    trailheads = []

    for i in range(len(topographic_map)):  # row
        for j in range(len(topographic_map[0])):  # column
            if topographic_map[i][j] == 0:
                trailheads.append((i, j))

    return trailheads


def find_paths(topographic_map, trailheads) -> int:
    score = 0
    for trailhead in trailheads:
        peaks_generators = check_surroundings(topographic_map, trailhead, 0)

        # unpack generators
        peaks_actual = []
        for peaks in peaks_generators:
            peaks_actual.append(peaks)

        score += len(set(peaks_actual))

    return score


def find_paths_p2(topographic_map, trailheads) -> int:
    score = 0
    for trailhead in trailheads:
        peaks_generators = check_surroundings(topographic_map, trailhead, 0)

        # unpack generators
        peaks_actual = []
        for peaks in peaks_generators:
            peaks_actual.append(peaks)
        score += len(peaks_actual)  # Well, that was simple

    return score


def check_surroundings(topographic_map, location, height):
    if height == 9:
        yield location

    valid_steps = []

    # up
    if location[0] - 1 >= 0 and topographic_map[location[0] - 1][location[1]] == height + 1:
        valid_steps.append((location[0] - 1, location[1]))
    # down
    if location[0] + 1 < len(topographic_map) and topographic_map[location[0] + 1][location[1]] == height + 1:
        valid_steps.append((location[0] + 1, location[1]))
    # right
    if location[1] + 1 < len(topographic_map[0]) and topographic_map[location[0]][location[1] + 1] == height + 1:
        valid_steps.append((location[0], location[1] + 1))
    # left
    if location[1] - 1 >= 0 and topographic_map[location[0]][location[1] - 1] == height + 1:
        valid_steps.append((location[0], location[1] - 1))

    for step in valid_steps:
        yield from check_surroundings(topographic_map, step, height + 1)


if __name__ == '__main__':
    # input
    get_input(10)
    with open(r'./inputs/d10.txt', 'r') as file:
        memory = file.read()

    memory = memory.split('\n')
    memory = [list(x) for x in memory]
    memory = [[int(x) if x != '.' else x for x in y] for y in memory]

    trailheads = find_trailheads(memory)

    # Part 1
    score = find_paths(memory, trailheads)
    print('Part 1:', score)

    # Part 2
    score = find_paths_p2(memory, trailheads)
    print('Part 2:', score)
