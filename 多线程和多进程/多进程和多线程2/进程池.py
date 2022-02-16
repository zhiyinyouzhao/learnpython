import time
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

def task(num):
    print('执行',num)
    time.sleep(2)

if __name__ == '__main__':
    # pool = ProcessPoolExecutor(4)
    # for i in range(10):
    #     pool.submit(task,i)


    pool = ProcessPoolExecutor(4)
    for i in range(10):
        pool.submit(task,i)
    #等待进程池的任务都执行完毕后，再继续往下走
    pool.shutdown(True)
    print(1)

