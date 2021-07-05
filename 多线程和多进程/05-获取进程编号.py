# -*- coding: utf-8 -*-


import time
import multiprocessing
import os

# 唱歌
def sing(num,name):
    print '唱歌进程的pid:',os.getpid()
    print '唱歌进程的父进程pid:', os.getppid()
    for i in range(num):
        print name
        print "唱歌..."
        time.sleep(0.5)

# 跳舞
def dance(num,name):
    print '跳舞进程的pid:',os.getpid()
    # windows 没有getppid函数
    print os.getppid()
    #print '跳舞进程的父进程pid:',os.getppid()
    for i in range(num):
        print name
        print "跳舞..."
        time.sleep(0.5)


if __name__ == '__main__':
    print '主进程的pid:',os.getpid()
    # 2.使用进程类创建进程对象
    # target:指定进程执行的函数名
    # args:使用元祖方式给指定任务传参
    # kwargs:使用字典式给指定任务传参
    sing_process = multiprocessing.Process(target=sing,args=(3,"xiaoming"))
    dance_process = multiprocessing.Process(target=dance,kwargs={'name':'传智','num':2})

    # 3.使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()

