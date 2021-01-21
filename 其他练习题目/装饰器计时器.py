import time

def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(time.time() - start_time, 'time....')
    return wrapper


@count_time
def my_count():
    s = 0
    for i in range(1000001):
        s += i
    print(s)

my_count()
