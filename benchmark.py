def benchmark(function):
    from time import perf_counter
    def wrapper(*args):
        start = perf_counter()
        #print(args)
        print(function(*args))
        #function(*args)
        print(perf_counter() - start)
    return wrapper