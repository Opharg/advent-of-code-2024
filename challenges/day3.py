import re
import get_input

get_input.get_input(3)
with open(r'./inputs/d3.txt', 'r') as file:
    memory = file.read()

pattern_mul = re.compile(r'mul\([0-9]+,[0-9]+\)')
matches = re.findall(r'mul\([0-9]+,[0-9]+\)', memory)

total = 0
for match in matches:
    match = match[4:-1].split(',')
    total += int(match[0]) * int(match[1])

print(total)

# part 2

total = 0
do = True

while True:
    if memory.startswith('do()') and not memory.startswith("don't"):
        do = True
        memory = memory[4:]
        continue
    elif memory.startswith("don't()"):
        do = False
        memory = memory[7:]
        continue
    elif memory.startswith("mul("):
        if do:
            # print(memory[:20])
            num1 = re.match(pattern_mul, memory)
            if type(num1) is not type(None):
                num1 = num1.group()
                num1 = num1[4:-1].split(',')
                total += int(num1[0]) * int(num1[1])
    memory = memory[1:]

    if len(memory) < 5:
        break

print(total)
