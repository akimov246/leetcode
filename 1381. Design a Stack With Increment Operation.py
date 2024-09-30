class CustomStack:

    def __init__(self, maxSize: int):
        self.__stack = []
        self.max_size = maxSize

    @property
    def stack(self):
        return self.__stack

    @property
    def max_size(self):
        return self.__max_size

    @max_size.setter
    def max_size(self, value):
        if value > 0:
            self.__max_size = value
        else:
            raise ValueError

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val