# -*- coding: utf-8 -*-


import time
import multiprocessing

# 唱歌
def sing(num,name):
    for i in range(num):
        print("%s唱歌..." %name)
        time.sleep(0.5)

# 跳舞
def dance(num):
    for i in range(num):
        print("跳舞...")
        time.sleep(0.5)


if __name__ == '__main__':
    # 2.使用进程类创建进程对象
    # target:指定进程执行的函数名
    # args:使用元祖方式给指定任务传参
    # kwargs:使用字典式给指定任务传参
    sing_process = multiprocessing.Process(target=sing,args=(3,'小明'))
    dance_process = multiprocessing.Process(target=dance,kwargs={'num':2})

    # 3.使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()