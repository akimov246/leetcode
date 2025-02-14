class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.__start_idx = 0

    def add(self, num: int) -> None:
        self.stream.append(1)
        if num != 1:
            for i in range(self.__start_idx, len(self.stream)):
                self.stream[i] *= num
        if num == 0:
            self.__start_idx = len(self.stream)

    def getProduct(self, k: int) -> int:
        return self.stream[len(self.stream) - k]

obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)