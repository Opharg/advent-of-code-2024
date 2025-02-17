from get_input import get_input


def process_input(memory):
    machines = []

    for line in memory:

        match line.split(':')[0]:
            case 'Button A':
                line = line.split('+')
                ax = int(line[1][:-3])
                ay = int(line[2])
            case 'Button B':
                line = line.split('+')
                bx = int(line[1][:-3])
                by = int(line[2])
            case 'Prize':
                line = line.split('=')
                px = int(line[1][:-3])
                py = int(line[2])
                machines.append((ax, ay, bx, by, px, py))
            case _:
                pass

    return machines


def simulate_machines(memory) -> int:
    total_cost = 0

    for machine in memory:
        total_cost += simulate_single_machine(machine)

    return total_cost


def simulate_single_machine(specifications) -> int:
    valid_results = []
    ax, ay, bx, by, px, py = specifications

    # naive 100, p2 isn't gonna bite me
    for i in range(0, 100):  # A
        for j in range(0, 100):  # B
            a = (ax * i) + (bx * j)
            b = (ay * i) + (by * j)
            if ((ax * i) + (bx * j) == px) and ((ay * i) + (by * j) == py):
                valid_results.append((i, j))

    if len(valid_results) == 0: return 0

    # a, b, price
    cheapest_move = 0
    for result in valid_results:
        cost = calculate_tokens(result)
        if cost > cheapest_move:
            cheapest_move = cost

    return cheapest_move


def calculate_tokens(moves) -> int:
    return moves[0] * 3 + moves[1]


if __name__ == '__main__':
    # input
    get_input(13)
    with open(r'./inputs/d13.txt', 'r') as file:
        memory = file.read()

    memory = memory.split('\n')
    memory = process_input(memory)
    part_1 = simulate_machines(memory)
    print('Part 1:', part_1)
