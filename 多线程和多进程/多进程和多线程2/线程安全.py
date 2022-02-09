
'''
    一个进程中可以有多个线程，且线程共享所有进程中的资源
    多个线程同时去操作一个东西，可能存在数据混乱的情况
'''

import threading

lock_obj = threading.RLock()
loop = 100000
number = 0

def add(count):
    lock_obj.acquire()  #申请锁
    global number
    for i in range(count):
        number += 1
    lock_obj.release()  #释放锁

def sub(count):
    lock_obj.acquire()  #申请锁
    global number
    for i in range(count):
        number -= 1
    lock_obj.release()  #释放锁

if __name__ == '__main__':
    t1 = threading.Thread(target=add,args=(loop,))
    t2 = threading.Thread(target=sub, args=(loop,))
    t1.start()
    t2.start()
    t1.join()       #t1线程执行完毕，才会继续往下走
    t2.join()       #t1线程执行完毕，才会继续往下走
    print(number)