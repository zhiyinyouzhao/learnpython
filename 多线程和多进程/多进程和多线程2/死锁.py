
'''
    死锁：由于竞争资源或者由于彼此通信而造成的一种阻塞的现象。
'''

import threading
import time
num = 0
lock_obj = threading.Lock()
lock_obj1 = threading.RLock()
lock_1 = threading.Lock()
lock_2 = threading.Lock()


def task():
    print("开始")
    lock_obj.acquire()      #第1个抵达的线程进入并上锁，其他线程就需要再次等待
    lock_obj.acquire()      #第1个抵达的线程进入并上锁，其他线程就需要再次等待
    global num
    for i in  range(1000000):
        num += 1
    lock_obj.release()      #线程出去，并解开锁，其他线程就可以进入并执行了
    lock_obj.release()      #线程出去，并解开锁，其他线程就可以进入并执行了
    print(num)

def task1():
    lock_1.acquire()
    time.sleep(1)
    lock_2.acquire()
    print(11)
    lock_2.release()
    print(111)
    lock_1.release()
    print(1111)

def task2():
    lock_2.acquire()
    time.sleep(1)
    lock_1.acquire()
    print(11)
    lock_1.release()
    print(111)
    lock_2.release()
    print(1111)



if __name__ == '__main__':
    # for i in range(2):
    #     t = threading.Thread(target=task)
    #     t.start()
    #
    # for i in range(2):
    #     t = threading.Thread(target=task)
    #     t.start()
    t1 = threading.Thread(target=task1)
    t1.start()
    t2 = threading.Thread(target=task2)
    t2.start()
