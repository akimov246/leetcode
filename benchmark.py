def benchmark(function):
    from time import perf_counter
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        print(perf_counter() - start)
        return result
    return wrapper


def pasths(x: int, y: int):
    d = {(i, j): None for i in range(1, x + 1)
                      for j in range(1, y + 1)}
    return helper(x, y, d)

def helper(x: int, y: int, d: dict):
    if x < 1 or y < 1:
        return 0
    if x == 1 and y == 1:
        return 1
    if d.get((x, y)):
        return d.get((x, y))
    d[(x, y)] = helper(x - 1, y, d) + helper(x, y - 1, d)
    return d.get((x, y))
