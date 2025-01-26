import get_input
get_input.get_input(4)

with open(r'./inputs/d4.txt', 'r') as file:
    memory = file.read()

xmas_count = 0
column_count = memory.find('\n') + 1  # \n is last column (except in the last line...)
row_count = memory.count('\n') + 1
#print(f'Column count: {column_count}')
#print(f'Row count: {row_count}')

# backwards/forward search
#print('backwards/forward locations:')
for row in range(row_count):
    for column in range(column_count - 4):
        cutout = memory[column_count * row + column:column_count * row + column + 4]
        if cutout == 'XMAS' or cutout == 'SAMX':
            #print(cutout + 4], row, column)
            xmas_count += 1

# down/up search
#print('down/up locations:')
for row in range(row_count - 3):
    for column in range(column_count - 1):
        # to safe my sanity reading
        cutout = memory[column_count * row + column] \
                 + memory[column_count * (row + 1) + column] \
                 + memory[column_count * (row + 2) + column] \
                 + memory[column_count * (row + 3) + column]

        if cutout == 'XMAS' or cutout == 'SAMX':
            #print(cutout, row, column)
            xmas_count += 1

# diagonal top-left -> down-right
#print('diagonal top-left -> down-right locations:')
for row in range(row_count - 3):
    for column in range(column_count - 4):
        # to safe my sanity reading
        cutout = memory[column_count * row + column] \
                 + memory[column_count * (row + 1) + column + 1] \
                 + memory[column_count * (row + 2) + column + 2] \
                 + memory[column_count * (row + 3) + column + 3]

        if cutout == 'XMAS' or cutout == 'SAMX':
            #print(cutout, row, column)
            xmas_count += 1

# diagonal top-right -> down-left
#print('diagonal top-right -> down-left locations:')
for row in range(row_count - 3):
    for column in range(3, column_count):
        # to safe my sanity reading
        cutout = memory[column_count * row + column] \
                 + memory[column_count * (row + 1) + column - 1] \
                 + memory[column_count * (row + 2) + column - 2] \
                 + memory[column_count * (row + 3) + column - 3]

        if cutout == 'XMAS' or cutout == 'SAMX':
            #print(cutout, row, column)
            xmas_count += 1

print('Part1: ', xmas_count)

# part 2
mas_count = 0
for row in range(row_count - 2):
    for column in range(column_count - 3):
        # to safe my sanity reading

        cutout_dr = memory[column_count * row + column] \
                    + memory[column_count * (row + 1) + column + 1] \
                    + memory[column_count * (row + 2) + column + 2]
        cutout_dl = memory[column_count * row + column + 2] \
                    + memory[column_count * (row + 1) + column + 1] \
                    + memory[column_count * (row + 2) + column]

        if (cutout_dl == 'MAS' or cutout_dl == 'SAM') and (cutout_dr == 'MAS' or cutout_dr == 'SAM'):
            #print(cutout_dr, cutout_dl, row, column)
            mas_count += 1

print('Part2: ', mas_count)
