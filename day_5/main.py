from day_5.plane import Plane
from day_5.seat import Seat
import pandas as pd


def get_data(input_path):
    with open(input_path, "r") as inputFile:
        data = inputFile.read().splitlines()
    return data


def run():
    data = get_data("./data/input")

    rows = 128
    columns = 8

    plane = Plane(rows, columns)
    for entry in data:
        plane.occupy_seat_by_binary_pattern(entry)

    pd.set_option("max_rows", None)
    df = pd.DataFrame(plane.get_readable_seat_grid(), index=range(rows), columns=range(columns))
    print(f'plane:')
    print(df)

    print(f'data length: {len(data)}')
    print(f'amount of seats: {rows * columns}')
    print(f'free seats: {plane.free_seats()}')
    print(f'occupied seats: {plane.occupied_seats()}')
    print(f'sum: {plane.free_seats() + plane.occupied_seats()}')
    print(f'seat with highest id:\n\tid: {plane.get_seat_with_highest_id().id}\n\trow: '
            f'{plane.get_seat_with_highest_id().row} (+1)\n'
            f'\tcolumn: {plane.get_seat_with_highest_id().column} (+1)')
    print(f'free seat within occupied seats:\n\tid: {plane.get_only_free_seat_between_occupied().id}\n\trow: '
          f'{plane.get_only_free_seat_between_occupied().row} (+1)\n'
          f'\tcolumn: {plane.get_only_free_seat_between_occupied().column} (+1)')

    with open('results.txt', 'w') as f:
        f.write(f'plane:\n')
        f.write(df.__str__())
        f.write(f'\n')
        f.write(f'data length: {len(data)}\n')
        f.write(f'amount of seats: {rows * columns}\n')
        f.write(f'free seats: {plane.free_seats()}\n')
        f.write(f'occupied seats: {plane.occupied_seats()}\n')
        f.write(f'sum: {plane.free_seats() + plane.occupied_seats()}\n')
        f.write(f'seat with highest id:\n\tid: {plane.get_seat_with_highest_id().id}\n\trow: '
                f'{plane.get_seat_with_highest_id().row} (+1)\n'
                f'\tcolumn: {plane.get_seat_with_highest_id().column} (+1)\n')
        f.write(f'free seat within occupied seats:\n\tid: {plane.get_only_free_seat_between_occupied().id}\n\trow: '
                f'{plane.get_only_free_seat_between_occupied().row} (+1)\n'
                f'\tcolumn: {plane.get_only_free_seat_between_occupied().column} (+1)\n')


if __name__ == '__main__':
    run()
