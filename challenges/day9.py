from get_input import get_input


def generate_disk(disk_map) -> list:
    disk = []
    id = 0
    for idx, e in enumerate(disk_map):
        if idx % 2 == 0:
            for _ in range(e):
                disk.append(id)
            id += 1
        else:
            for _ in range(0, e):
                disk.append(None)

    return disk


def shift_blocks(disk) -> list:
    idx = 0
    while True:
        try:
            idx = disk.index(None)
        except ValueError:
            break
        disk[idx] = disk[-1]
        disk.pop()

    return disk


def shift_files(disk_map, disk) -> list:
    # I should probably do something like sum(updated_local_map[:current_index], but I didn't.
    local_map = [x for x in disk_map]
    current_id = len(local_map) // 2

    while current_id > 0:
        original_location = disk.index(current_id)
        file_size = local_map[current_id * 2]
        free_block = [None] * file_size

        idx = sublist_with_index(disk, free_block)
        if idx and idx < original_location:
            for i in range(file_size):
                disk[idx + i] = current_id
                disk[original_location + i] = None

        current_id -= 1

    return disk


def sublist_with_index(list, sublist) -> int | None:
    offset = len(sublist)
    for idx in range(len(list) - offset):
        if sublist == list[idx:idx + offset]:
            return idx
    return None  # could return 0 for static typing


def calculate_checksum(disk):
    checksum = 0
    for idx, e in enumerate(disk):
        if e is not None:
            checksum += idx * e

    return checksum


if __name__ == '__main__':
    # input
    get_input(9)
    with open(r'./inputs/d9.txt', 'r') as file:
        disk_map = list(file.read())
        disk_map = [int(x) for x in disk_map]

    # Part 1
    disk = generate_disk(disk_map)
    disk = shift_blocks(disk)
    checksum = calculate_checksum(disk)
    print('Part 1:', checksum)

    # Part 2
    disk = generate_disk(disk_map)
    disk = shift_files(disk_map, disk)
    checksum = calculate_checksum(disk)
    print('Part 2:', checksum)
