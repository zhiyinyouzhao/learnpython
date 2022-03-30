
import time


def outer(f):
    def inner():
        start_time = time.perf_counter()
        f()
        end_time = time.perf_counter()
        return end_time-start_time
    return inner

@outer
def count():
    for i in range(10):
        print(i)
        time.sleep(1)

if __name__ == '__main__':
    print(count())
