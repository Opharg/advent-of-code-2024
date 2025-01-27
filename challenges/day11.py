from functools import cache

from get_input import get_input

cache_p1 = {}


def single_blink(stone):
    if stone in cache_p1:
        return cache_p1[stone]

    if stone == 0:
        cache_p1[stone] = {1}
        return cache_p1[stone]

    if len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        cache_p1[stone] = (
            int(stone_str[:len(stone_str) // 2]),
            int(stone_str[len(stone_str) // 2:])
        )
        return cache_p1[stone]

    cache_p1[stone] = {stone * 2024}
    return cache_p1[stone]


def blink(memory):
    new_memory = []

    for stone in memory:
        new_memory.extend(single_blink(stone))

    return new_memory


@cache
def blink_recursive(stone, depth):
    # length = len(str(stone))
    # if depth == 1 and length % 2 == 0:
    #     return 2  # lucky? Could be 2, no?
    # elif depth == 0:
    #     return 1

    # one additional blink to not compute length every run, those micro-optimizations...
    if depth == 0:
        return 1

    if stone == 0:
        return blink_recursive(1, depth - 1)

    length = len(str(stone))
    if length % 2 == 0:
        stone1 = int(str(stone)[:length // 2])
        stone2 = int(str(stone)[length // 2:])
        return blink_recursive(stone1, depth - 1) + blink_recursive(stone2, depth - 1)

    return blink_recursive(stone * 2024, depth - 1)


if __name__ == '__main__':
    # input
    get_input(11)
    with open(r'./inputs/d11.txt', 'r') as file:
        memory = file.read()

    memory = memory.split(" ")
    memory = [int(x) for x in memory]

    # Part 1
    BLINK_AMOUNT = 25
    memory_p1 = memory
    for _ in range(BLINK_AMOUNT):
        memory_p1 = blink(memory_p1)
    print('Part 1:', len(memory_p1))

    # Part 2
    # looked online to find that recursion is apparently faster. Makes sense; counting stones, instead of lighting up RAM.
    # Also, dict cache doesn't work, so I just went with functools.
    BLINK_AMOUNT = 75
    length = 0
    for stone in memory:
        length += blink_recursive(stone, BLINK_AMOUNT)

    print('Part 2:', length)
