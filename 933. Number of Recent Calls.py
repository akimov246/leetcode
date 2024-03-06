class RecentCounter:

    __slots__ = ('requests')

    def __init__(self):
        self.requests = []

    def __repr__(self):
        return str(self.requests)

    def ping(self, t: int) -> int:
        RANGE = t - 3000
        self.requests.append(t)
        for i in range(len(self.requests)):
            if self.requests[i] >= RANGE:
                self.requests = self.requests[i:]
                return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
obj.ping(1)
obj.ping(100)
obj.ping(3001)
print(obj.ping(3002))