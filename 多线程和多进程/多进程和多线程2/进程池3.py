
'''
    如果进程池中要使用进程锁，则需要基于Manager中的Lock和Rlock来实现
    不能使用multiprocessing.RLock()
'''

import time
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor


def task(lock):
    print("开始")
    with lock:
        #假设文件中保存的内容就是一个值：10
        with open('f1.txt',mode='r',encoding='utf-8') as f:
            current_num = int(f.read())
        print('排队抢票了')
        time.sleep(1)
        current_num -= 1

        with open('f1.txt',mode='w',encoding='utf-8') as f:
            f.write((str(current_num)))


if __name__ == '__main__':
    pool = ProcessPoolExecutor()
    manager = multiprocessing.Manager()
    lock_obj = manager.RLock()
    for i in range(10):
        pool.submit(task,lock_obj)


