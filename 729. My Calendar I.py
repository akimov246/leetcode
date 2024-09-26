class MyCalendar:

    def __init__(self):
        self.books = set()

    def __repr__(self):
        return f'{self.books}'

    def book(self, start: int, end: int) -> bool:
        if not self.books:
            self.books.add((start, end - 1))
            return True

        for s, e in self.books:
            if (s <= start <= e) or (s <= end - 1 <= e) or (start <= s and end - 1 >= e):
                return False
        self.books.add((start, end - 1))
        return True


# Your MyCalendar object will be instantiated and called as such:
#obj = MyCalendar()
# print(obj.book(10, 20))
# print(obj.book(15, 25))
# print(obj.book(20, 30))