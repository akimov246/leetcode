from typing import Callable
import functools

def benchmark(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        arg_lst = [str(arg) for arg in args]
        arg_lst.extend([f'{k}={v}' for k, v in kwargs.items()])
        arg_str = ', '.join(arg_lst)
        name = func.__name__
        print(f'Время выполнения {name}({arg_str}): {time.perf_counter() - start:.05f} -> {result}')
        return result
    return wrapper

@functools.cache
@benchmark
def f(n):
    if n == 0 or n == 1:
        return 1
    return f(n - 2) + f(n - 1)

#print(f(650))

def fdp(n):
    if n < 2:
        return 1
    fs = [None] * n
    fs[0] = fs[1] = 1
    for i in range(2, n, 1):
        if i % 2 == 0:
            fs[i] = fs[i // 2] + fs[i // 2 - 1]
        else:
            fs[i] = fs[(i - 1) // 2] + fs[(i - 1) // 2 - 1]

    return fs[n - 1]

print(fdp(10))
