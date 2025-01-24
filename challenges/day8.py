from get_input import get_input

# global
antinodes = set()

def find_antinodes(antenna, p2):
    for location in antennas[antenna]:
        for also_location in antennas[antenna]:
            # looping twice to check a->b b->a for easier math and less code
            if location == also_location:
                continue

            vertical_distance = location[0] - also_location[0]
            horizontal_distance = location[1] - also_location[1]

            if p2:
                scalar = 1
                while True:
                    if (0 <= location[0] + vertical_distance * scalar < height and
                            0 <= location[1] + horizontal_distance * scalar < width):
                        antinodes.add((location[0] + vertical_distance * scalar,
                                       location[1] + horizontal_distance * scalar))
                        scalar += 1
                    else:
                        break
            else:
                if (0 <= location[0] + vertical_distance < height and
                        0 <= location[1] + horizontal_distance < width):
                    antinodes.add((location[0] + vertical_distance,
                                   location[1] + horizontal_distance))


def find_antennas():
    antennas = {}
    count = 0

    for i in range(len(memory)):  # row
        for j in range(width):  # column
            if memory[i][j] != '.' and memory[i][j] != '#':
                count += 1

                if memory[i][j] not in antennas:  # create dict entry
                    antennas[memory[i][j]] = [(i, j)]
                else:  # use existing dict entry
                    antennas[memory[i][j]].append((i, j))

    return count, antennas


if __name__ == '__main__':

    # input
    get_input(8)
    with open(r'./inputs/d8.txt', 'r') as file:
        memory = file.read()

    memory = memory.split('\n')
    memory = [list(x) for x in memory]

    width = len(memory[0])
    height = len(memory)

    antennas_counter, antennas = find_antennas()

    # p1
    for antenna in antennas:
        find_antinodes(antenna, False)

    print('Part 1: ')
    print(len(antinodes))

    # p2
    antinodes = set()
    for antenna in antennas:
        find_antinodes(antenna, True)

        # add antennas to antinodes set
        for location in antennas[antenna]:
            antinodes.add(location)

    print('Part 2: ')
    print(len(antinodes))
