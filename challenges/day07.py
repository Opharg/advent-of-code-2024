from get_input import get_input

# global, so I don't have to pass it around
combinations_cache = {}


def generate_combinations(operators, length):
    global combinations_cache
    combinations = [x for x in operators]
    for _ in range(length - 2):
        temp = []
        for combination in combinations:
            for op in operators:
                temp.append(combination + op)
        combinations = temp

    combinations_cache[length] = combinations


def get_valid_results(equation, operators):
    left = equation[0]
    values = equation[1]

    # pre-compute combinations
    if len(values) not in combinations_cache:
        generate_combinations(operators, len(values))

    for combination in combinations_cache[len(values)]:
        # calculate in sequence, not according to precedence rules
        term_result = values[0]
        for idx, op in enumerate(combination):
            try:
                match op:
                    case "+":
                        term_result += values[idx + 1]
                    case '*':
                        term_result *= values[idx + 1]
                    case '|':
                        term_result = int(str(term_result) + str(values[idx + 1]))
            except Exception:
                print(equation, idx, values, combination)
                raise

        if left == term_result:
            return left


if __name__ == '__main__':

    # input
    get_input(7)
    with open(r'./inputs/d7.txt', 'r') as file:
        memory = file.read()
    memory = memory.split('\n')
    memory = [x.split(':') for x in memory]

    # conversion
    for equation in memory:
        equation[0] = int(equation[0])
        equation[1] = [int(x) for x in equation[1].strip().split(' ')]

    # operators
    operators_p1 = ['+', '*']
    # I ain't rewriting my string parsing to list to handle two chars^^
    operators_p2 = ['+', '*', '|']

    # part 1
    total = 0
    for equation in memory:
        result = get_valid_results(equation, operators_p1)
        if result:
            total += result
    print('part 1:', total)

    # part 2
    total = 0
    combinations_cache = {}  # this is important...
    for equation in memory:
        result = get_valid_results(equation, operators_p2)
        if result:
            total += result
    print('part 2:', total)
