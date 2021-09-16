
import time

def outer(f):
    def inner():
        start = time.perf_counter()
        f()
        end = time.perf_counter()
        return end-start
    return inner

@outer
def func():
    for i in range(10):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    # func = outer(func)
    print(func())

