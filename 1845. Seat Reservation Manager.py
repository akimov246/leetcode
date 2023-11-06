class SeatManager(object):
    def __init__(self, n: int):
        self.n = self._is_valid_n(n)
        self.seats = dict.fromkeys(range(1, self.n+1), False)

    def _is_valid_n(self, n):
        if n < 1:
            raise ValueError("Сидений не может быть меньше одного")
        return n

    def reserve(self) -> int:
        if self.n == 1:
            self.seats.update({1: True})
            return 1
        for seat in self.seats.keys():
            if not self.seats.get(seat):
                self.seats[seat] = True
                return seat

    def unreserve(self, seatNumber: int) -> None:
        if self.seats.get(seatNumber):
            self.seats[seatNumber] = False

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

obj = SeatManager(5)
print(obj.seats)
obj.reserve()
obj.reserve()
obj.unreserve(1)
print(obj.seats)