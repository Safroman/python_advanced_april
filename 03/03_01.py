from random import randint
import time


def outer_time_func(iterations):

    def inner_time_func(func):

        def wrapper(*args, **kwargs):
            total = 0

            for i in range(iterations):
                start_time = time.time()
                func(*args, **kwargs)
                total += (time.time() - start_time)

            print(f'function "{func.__name__}" blended runtime is  {total / iterations} sec')

        return wrapper

    return inner_time_func


@outer_time_func(3)
def test_func_1():
    counter = 0

    for i in range(0, randint(100, 10000)):
        counter += i
    pass


@outer_time_func(3)
def test_func_2(a, b):
    total = 0

    for i in range(0, randint(100, 10000)):
        total += (a**i + b)**i
    pass


test_func_1()

test_func_2(1, 10)


