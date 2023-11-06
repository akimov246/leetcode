import numpy

class SeatManager:

    def __init__(self, n: int):
        self.n = self._is_valid_n(n)
        #self.unreserved_seats = numpy.arange(1, self.n + 1, dtype="int32")
        self.unreserved_seats = numpy.arange(self.n, 0, -1, dtype='int32')
        print(self.unreserved_seats)

    def _is_valid_n(self, n: int) -> int:
        if n < 1:
            raise ValueError
        return n

    def reserve(self) -> int:
        seatNumber = numpy.min(self.unreserved_seats)
        index = numpy.where(self.unreserved_seats == seatNumber)
        self.unreserved_seats = numpy.delete(self.unreserved_seats, index)
        return seatNumber

    def unreserve(self, seatNumber: int) -> None:
        index = numpy.where(self.unreserved_seats == seatNumber)
        if not len(index[0]):
            self.unreserved_seats = numpy.append(self.unreserved_seats, seatNumber)


import random
import time

# obj = SeatManager(5)
# print(obj.reserve())
# print(obj.reserve())
# obj.unreserve(1)
# obj.unreserve(1)
# #print(obj.reserve())
# #print(obj.reserve())
# print(obj.unreserved_seats)


N = 100000
start = time.perf_counter()
obj = SeatManager(N)
for i in range(N):
    r = random.randint(1, N)
    action = ["obj.reserve()", f"obj.unreserve({r})"]
    #action = ["obj.reserve()"]
    eval(random.choice(action))
print(time.perf_counter() - start)

