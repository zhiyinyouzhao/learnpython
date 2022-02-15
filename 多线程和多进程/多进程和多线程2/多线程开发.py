
import threading

'''
    GIL:一个进程中统一时刻只有一个线程可以被CPU调度，所以
        计算密集型，适合用于多进程开发
        IO密集型，适合用多线程开发
    t.start()   当前线程准备就绪（等待cpu调度，具体时间由cpu决定）
    t.join()    等待当前线程的任务执行完毕后再向下继续执行
'''

loop = 10000000
number = 0

def add(count):
    global number
    for i in range(count):
        number += 1

def add1():
    global number
    for i in range(100000):
        number += 1

if __name__ == '__main__':
    # t = threading.Thread(target=add,args=(loop,))
    # t.start()
    # print(number)
    t = threading.Thread(target=add1)
    t.start()
    t.join()    #主线程等待中....
    print(number)


