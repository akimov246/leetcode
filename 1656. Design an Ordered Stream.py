class OrderedStream:

    def __repr__(self):
        return f'{self.stream}'

    def __init__(self, n: int):
        self.n = n
        self.stream = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey - 1] = value
        result = []
        for i in range(self.ptr, self.n):
            if self.stream[i]:
                result.append(self.stream[i])
                self.ptr += 1
            else:
                break
        return result

# Your OrderedStream object will be instantiated and called as such:
obj = OrderedStream(5)
param_1 = obj.insert(3, 'ccccc')
param_2 = obj.insert(1, 'aaaaa')
param_3 = obj.insert(2, 'bbbbb')
param_4 = obj.insert(5, 'eeeee')
param_5 = obj.insert(4, 'ddddd')