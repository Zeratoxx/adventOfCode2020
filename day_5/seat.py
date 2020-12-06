from enum import Enum


class SeatStatus(Enum):
    free = 1
    occupied = 2


class Seat:
    row_multiplier = 8

    def __init__(
            self, row, column
    ):
        self.status = SeatStatus.free
        self.row = row
        self.column = column
        self.id = -1
        self.__set_seat_id()

    def __set_seat_id(self):
        self.id = self.row * self.row_multiplier + self.column
