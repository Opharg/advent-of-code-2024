import get_input
get_input.get_input(5)

with open(r'./inputs/d5.txt', 'r') as file:
    memory = file.read()

memory = memory.split('\n\n')
instructions = memory[0].split('\n')
updates = memory[1].split('\n')

# format data into 2d arrays
for i in range(len(instructions)):
    instructions[i] = instructions[i].split('|')
for i in range(len(updates)):
    updates[i] = updates[i].split(',')


def check_failed(update):
    for idx, page in enumerate(update):
        for instruction in instructions:
            if page == instruction[1] and instruction[0] in update[idx:]:  # str btw
                return page, idx, instruction[0]  # "not None" for p1, data for p2


middle_numbers = []
for update in updates:
    failed = check_failed(update)
    if not failed:
        middle_numbers.append(int(update[len(update) // 2]))

print(sum(middle_numbers))

# part 2
middle_numbers_p2 = []
for update in updates:

    failed_once = False
    while check_failed(update):
        failed_once = True
        failed = check_failed(update)

        # swap offending page with page that should come before it
        target_idx = update.index(failed[2])
        update[failed[1]], update[target_idx] = update[target_idx], update[failed[1]]

    if failed_once:
        middle_numbers_p2.append(int(update[len(update) // 2]))

print(sum(middle_numbers_p2))

