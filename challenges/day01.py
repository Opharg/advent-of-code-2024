import get_input
get_input.get_input(1)

l1 = []
l2 = []
distance = 0

with open(r'./inputs/d1.txt', 'r') as file:
    for line in file:
        l1.append(int(line[0:5]))
        l2.append(int(line[8:13]))

l1.sort()
l2.sort()

for a, b in zip(l1, l2):
    distance += abs(a - b)

print(distance)

# part 2
counts = {}
similarity = 0
for num in l2:
    counts[num] = counts.get(num, 0) + 1

for num in l1:
    if num in counts:
        similarity += num * counts[num]

print(similarity)
