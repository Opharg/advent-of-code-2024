import os
from aocd import get_data

def get_input(day):
    if not os.path.exists('./inputs'):
        os.mkdir('./inputs')

    if os.path.isfile(fr'./inputs/d{day}.txt'):
        print(f'Input for day {day} found')
        return

    try:

        data = get_data(day=day, year=2024)
        # Open the local file to write the downloaded content
        with open(fr'./inputs/d{day}.txt', 'w') as file:
            file.write(data)
            print(f'Input for day {day} fetched')

        return True
    except Exception as e:
        print(f"Error downloading input for day {day}: {e}")
        raise