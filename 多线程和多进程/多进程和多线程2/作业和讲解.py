

''''
    程序从flag a执行到flag b的时间大致是多少秒？
    确认执行到最后number是否一定为0？
'''


import threading
import time

def wait():
    time.sleep(60)

loop = int(1E7)
number = 0

def add(loop = 1):
    global number
    for _ in range(loop):
        number += 1

def sub(loop = 1):
    global number
    for _ in range(loop):
        number -= 1


if __name__ == '__main__':
    '''E
    # 60秒
    # flag a
    t1 = threading.Thread(target=wait)
    t1.setDaemon(False) 
    t1.start()
    # flag b
    '''

    '''
    # 0秒
    # flag a
    t1 = threading.Thread(target=wait)
    t1.setDaemon(True)
    t1.start()
    # flag b
    '''

    '''
    # 60秒
    # flag a
    t1 = threading.Thread(target=wait)
    t1.start()
    t1.join()  #等待当前线程的任务执行完毕后再向下继续执行
    # flag b
    '''

    '''
    # number为0
    ta = threading.Thread(target=add,args=(loop,))
    ts = threading.Thread(target=sub,args=(loop,))
    ta.start()
    ta.join()
    ts.start()
    ts.join()
    '''

    '''
    # number不一定为0
    ta = threading.Thread(target=add,args=(loop,))
    ts = threading.Thread(target=sub,args=(loop,))
    ta.start()
    ts.start()
    ta.join()
    ts.join()
    '''


