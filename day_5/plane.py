from day_5.seat import Seat, SeatStatus


class Plane:

    def __init__(self, rows, columns):
        self.amount_rows = rows
        self.amount_columns = columns
        self.seat_grid = self.__init_seat_grid()

    def __init_seat_grid(self):
        grid = []
        for x in range(self.amount_rows):
            grid.append([])
            for y in range(self.amount_columns):
                grid[x].append(Seat(x, y))
        return grid

    def get_readable_seat_grid(self):
        string_list = []
        for x in range(len(self.seat_grid)):
            string_list.append([])
            for y in range(len(self.seat_grid[x])):
                if self.seat_grid[x][y].status == SeatStatus.free:
                    string_list[x].append("O")
                else:
                    string_list[x].append("X")
        return string_list

    def get_seat_grid(self):
        return self.seat_grid

    def occupy_seat_by_binary_pattern(self, seat_information_string):
        coordinates = self.__get_row_and_column(seat_information_string)
        column = coordinates["column"]
        row = coordinates["row"]
        return self.occupy_seat_by_row_and_column(row, column)

    def occupy_seat_by_row_and_column(self, row, column):
        if column != -1 and row != -1:
            if self.seat_grid[row][column].status == SeatStatus.free:
                self.seat_grid[row][column].status = SeatStatus.occupied
                return True
            else:
                return False
        else:
            return False

    def clear_seat_by_binary_pattern(self, seat_information_string):
        coordinates = self.__get_row_and_column(seat_information_string)
        column = coordinates["column"]
        row = coordinates["row"]
        return self.clear_seat_by_row_and_column(row, column)

    def clear_seat_by_row_and_column(self, row, column):
        if column != -1 and row != -1:
            if self.seat_grid[row][column].status == SeatStatus.occupied:
                self.seat_grid[row][column].status = SeatStatus.free
                return True
            else:
                return False
        else:
            return False

    def __get_row_and_column(self, seat_information_string):
        lower_row = 0
        upper_row = self.amount_rows - 1
        counter = 0
        for char in seat_information_string[:-3]:
            counter += 1
            if char == "F":
                upper_row -= self.amount_rows / (2 ** counter)
            elif char == "B":
                lower_row += self.amount_rows / (2 ** counter)
            else:
                raise ValueError
        first_column_left = 0
        last_column_left = self.amount_columns - 1
        counter = 0
        for char in seat_information_string[-3:]:
            counter += 1
            if char == "L":
                last_column_left -= self.amount_columns / (2 ** counter)
            elif char == "R":
                first_column_left += self.amount_columns / (2 ** counter)
            else:
                raise ValueError
        coordinates = {
            "row": -1,
            "column": -1
        }
        if last_column_left == first_column_left:
            coordinates["column"] = int(last_column_left)
        if upper_row == lower_row:
            coordinates["row"] = int(upper_row)
        return coordinates

    def free_seats(self):
        counter = 0
        for x in self.seat_grid:
            for y in x:
                if y.status == SeatStatus.free:
                    counter += 1
        return counter

    def occupied_seats(self):
        counter = 0
        for x in self.seat_grid:
            for y in x:
                if y.status == SeatStatus.occupied:
                    counter += 1
        return counter

    def get_seat_with_highest_id(self):
        for x in reversed(self.seat_grid):
            for y in reversed(x):
                if y.status == SeatStatus.occupied:
                    return y

    def get_only_free_seat_between_occupied(self):
        got_occupied = False
        for x in reversed(self.seat_grid):
            for y in reversed(x):
                if y.status == SeatStatus.occupied:
                    got_occupied = True
                if y.status == SeatStatus.free:
                    if got_occupied:
                        return y