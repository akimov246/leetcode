class SeatManager:

    def __init__(self, n: int):
        self.n = self._is_valid_n(n)
        self.min_seat = 1
        self.unreserved_seats = []

    def _is_valid_n(self, n: int) -> int:
        if n < 1:
            raise ValueError
        return n

    def reserve(self) -> int:
        seat = min(min(self.unreserved_seats, default=self.n + 1), self.min_seat)
        if seat in self.unreserved_seats:
            self.unreserved_seats.remove(seat)
            if seat < self.n + 1:
                return seat
        self.min_seat += 1
        if seat < self.n + 1:
            return seat

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber not in self.unreserved_seats:
            self.unreserved_seats.append(seatNumber)


import random
import time

# obj = SeatManager(5)
# print(obj.reserve())
# print(obj.reserve())
# obj.unreserve(1)
# obj.unreserve(1)
# obj.unreserve(2)
# print(obj.reserve())
# print(obj.reserve())
# print(obj.reserve())
# print(obj.reserve())
# print(obj.reserve())
# print(obj.reserve())
#print(obj.unreserved_seats)


N = 100000
start = time.perf_counter()
obj = SeatManager(N)
for i in range(N):
    r = random.randint(1, N)
    action = ["obj.reserve()", f"obj.unreserve({r})"]
    #action = ["obj.reserve()"]
    eval(random.choice(action))
print(time.perf_counter() - start)

