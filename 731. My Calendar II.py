class MyCalendarTwo:

    def __init__(self):
        self.books = set()
        self.double = set()

    def __repr__(self):
        return f'books:{self.books}, double:{self.double}'

    def book(self, start: int, end: int) -> bool:
        if not self.books:
            self.books.add((start, end - 1))
            return True

        for s, e in self.double:
            if (s <= start <= e) or (s <= end - 1 <= e) or (start <= s and end - 1 >= e):
                    return False

        for s, e in self.books:
            if s <= start <= e:
                self.double.add((start, min(e, end - 1)))
            elif s <= end - 1 <= e:
                self.double.add((max(start, s), end - 1))
            elif start <= s and end - 1 >= e:
                self.double.add((s, e))

        self.books.add((start, end - 1))
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendarTwo()
test = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
for start, end in test:
    print(obj.book(start, end))