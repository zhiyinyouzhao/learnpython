
'''
    在程序中如果想要自己手动加锁，一版有2种:Lock和Rlock
    Lock 同步锁
    Rlock 递归锁   支持多次申请锁和多次释放，lock不支持
'''

import threading
num = 0
lock_obj = threading.Lock()
lock_obj1 = threading.RLock()

def task():
    print("开始")
    lock_obj.acquire()  #第一个抵达的线程进入并上锁，其他线程就需要再次等待
    global num
    for i in range(1000000):
        num += 1
    lock_obj.release()  #线程出去，并解开锁，其他线程就可以进入并执行了
    print(num)


def task1():
    print("开始")
    lock_obj1.acquire()
    lock_obj1.acquire()
    print(123)
    lock_obj1.release()
    lock_obj1.release()


if __name__ == '__main__':
    # for i in range(2):
    #     t = threading.Thread(target=task)
    #     t.start()
    #
    for i in range(2):
        t = threading.Thread(target=task1)
        t.start()
