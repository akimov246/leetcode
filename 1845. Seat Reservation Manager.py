import array

class SeatManager:

    def __init__(self, n: int):
        self.n = self._is_valid_n(n)
        self.reserved_seats = []
        self.unreserved_seats = list(range(1, self.n + 1))

    def _is_valid_n(self, n: int) -> int:
        if n < 1:
            raise ValueError
        return n

    def reserve(self) -> int:
        seatNumber = min(self.unreserved_seats)
        self.reserved_seats.append(seatNumber)
        self.unreserved_seats.remove(seatNumber)
        return seatNumber

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber not in self.unreserved_seats:
            self.unreserved_seats.append(seatNumber)
            self.reserved_seats.remove(seatNumber)


import random
import time

N = 10000
start = time.perf_counter()
obj = SeatManager(N)
for i in range(N):
    r = random.randint(1, N)
    action = ["obj.reserve()", f"obj.unreserve({r})"]
    eval(random.choice(action))
print(obj.reserved_seats)
print(time.perf_counter() - start)

