

import multiprocessing
import threading
import time


def func():
    print("来了")
    # 都会被卡在这
    with lock:
        print(666)
        time.sleep(1)


def task():
    #拷贝的锁也是被申请走的状态
    #被谁申请走了呢？被子进程中的主线程申请走了
    print(lock)

    for i in range(10):
        t = threading.Thread(target=func)
        t.start()

    # lock.acquire()
    # print(666)  #可以输出

if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    name = []
    lock = threading.RLock()
    lock.acquire()  #申请锁
    p1 = multiprocessing.Process(target=task)
    p1.start()