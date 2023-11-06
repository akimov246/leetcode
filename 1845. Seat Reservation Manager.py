import numpy

class SeatManager:

    def __init__(self, n: int):
        self.n = self._is_valid_n(n)
        self.reserved_seats = numpy.array([], dtype="uint32")
        self.unreserved_seats = numpy.arange(1, self.n + 1, dtype="uint32")
        print(self.unreserved_seats)

    def _is_valid_n(self, n: int) -> int:
        if n < 1:
            raise ValueError
        return n

    def reserve(self) -> int:
        seatNumber = numpy.min(self.unreserved_seats)
        index = numpy.where(self.unreserved_seats == seatNumber)
        if index:
            self.reserved_seats = numpy.append(self.reserved_seats, seatNumber)
            self.unreserved_seats = numpy.delete(self.unreserved_seats, index)
            return seatNumber

    def unreserve(self, seatNumber: int) -> None:
        index = numpy.where(self.unreserved_seats == seatNumber)
        if index:
            self.unreserved_seats = numpy.append(self.unreserved_seats, seatNumber)
            index = numpy.where(self.reserved_seats == seatNumber)
            self.reserved_seats = numpy.delete(self.reserved_seats, index)


import random
import time

# obj = SeatManager(5)
# obj.reserve()
# print(obj.reserved_seats)
# obj.reserve()
# print(obj.reserved_seats)
# obj.unreserve(1)
# print(obj.reserved_seats)

N = 100000
start = time.perf_counter()
obj = SeatManager(N)
for i in range(N):
    r = random.randint(1, N)
    #action = ["obj.reserve()", f"obj.unreserve({r})"]
    action = ["obj.reserve()"]
    eval(random.choice(action))
print(obj.reserved_seats)
print(time.perf_counter() - start)

