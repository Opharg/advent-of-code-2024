import operator
import os
from functools import reduce
from time import sleep

import day13
from pprint import pprint

from get_input import get_input

WIDTH = 101
HEIGHT = 103
SECONDS = 100


class Robot:
    def __init__(self, name, px, py, vx, vy):
        self.name, self.px, self.py, self.vx, self.vy = name, px, py, vx, vy

    def __repr__(self):
        return f'{self.name}\t| Start: {self.px, self.py},\tVelocity: {self.vx, self.vy}'


def process_input(memory):
    memory = memory.split('\n')

    for idx, robot in enumerate(memory):
        p = robot.split('=')[1].split(',')
        v = robot.split('=')[2].split(',')
        memory[idx] = Robot(idx, int(p[0]), int(p[1][:-2]), int(v[0]), int(v[1]))

    return memory


def calculate_position(robot, seconds=1) -> (int, int):
    final_x = (robot.px + robot.vx * seconds) % WIDTH
    final_y = (robot.py + robot.vy * seconds) % HEIGHT
    return final_x, final_y


def simulate_robots(memory, spacemap, seconds=1) -> [int]:
    for robot in memory:
        position = calculate_position(robot, seconds=seconds)
        spacemap[position[1]][position[0]] += 1  # indeces flipped for print readability

    return spacemap


def count_quadrant(quadrant) -> int:
    count = 0
    for row in quadrant:
        count += sum(row)
    return count


def count_robots(space_map) -> tuple[int, int, int, int]:
    q1 = count_quadrant([row[0:WIDTH // 2] for row in space_map[0:HEIGHT // 2]])
    q2 = count_quadrant([row[WIDTH // 2 + 1:] for row in space_map[0:HEIGHT // 2]])
    q3 = count_quadrant([row[0:WIDTH // 2] for row in space_map[HEIGHT // 2 + 1:]])
    q4 = count_quadrant([row[WIDTH // 2 + 1:] for row in space_map[HEIGHT // 2 + 1:]])

    return q1, q2, q3, q4

def part_2(memory):
    bcolors = {
        '1': '\033[95m1' + '\033[0m',
        '2': '\033[94m2' + '\033[0m',
        '3': '\033[96m3' + '\033[0m',
        '4': '\033[92m4' + '\033[0m',
        '5': '\033[93m5' + '\033[0m'
    }

    seconds = 0
    matches = []
    while True:
        if seconds % 10 == 0:
            print(f'SECONDS: {seconds}')
        seconds += 1

        space_map = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
        space_map = simulate_robots(memory, space_map, seconds=seconds)

        # Simple pattern checks
        flag = False
        # Looking for clusters (so success)
        #for i in space_map:
        #    for j in i:
        #        if j > 0:
        #            flag = True

        # looking for lines
        space_map = [['#' if x > 0 else ' ' for x in y] for y in space_map]
        for line in space_map:
            line = "".join(line) + "|"
            if '#####' in line:
                flag = True

        if not flag:
            continue

        matches.append(seconds)  # to navigate backwards
        # Cluster colorization; pretty ineffective
        # space_map = [[bcolors[str(x)] if x > 0 else ' ' for x in y] for y in space_map]
        os.system('clear')
        print(matches[-10:])
        print(f'SECONDS: {seconds}')

        for line in space_map:
            print("".join(line) + "|")

        # navigate backwards on any input
        text = input()
        if len(text) > 0:
            seconds = matches[-2] - 1
            matches.pop()
            matches.pop()




def main():
    # input
    get_input(14)
    with open(r'./'
              r'inputs/d14.txt', 'r') as file:
        memory = file.read()
    memory = process_input(memory)

    # map
    # space_map = [[0] * HEIGHT] * WIDTH, doesn't work because it just references the same List WIDTH-times...
    space_map = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

    space_map = simulate_robots(memory, space_map, seconds=SECONDS)
    robot_count = count_robots(space_map)
    safety_factor = reduce(operator.mul, robot_count)
    print(f'Part 1: {safety_factor}')

    part_2(memory)

if __name__ == '__main__':
    main()
