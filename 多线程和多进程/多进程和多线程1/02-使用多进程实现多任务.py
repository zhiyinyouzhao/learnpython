# -*- coding: utf-8 -*-

'''
    多任务：
        1.并发-在一段时间内交替去执行多个任务
            例子：对于单核CPU处理多任务，操作系统轮流让各个任务交替执行
        2.并行-在一段时间内真正的同时一起执行多个任务
            例子：对于多核CPU处理多任务，操作系统会给CPU的每个内核安排一个执行的任务，多个内核是真正的一起同时执行多个任务。
                这里需要注意多核CPU是并行的执行多任务，始终有多个任务一起执行。

    进程：
        1.进程process是资源分配的最小单位，它是操作系统进行资源分配和调度运行的基本单位。
        2.通俗理解一个正在运行的程序就是一个进程，例如qq，微信都是一个进程。
        3.一个运行的程序至少有一个进程。
'''

'''
    进程创建步骤：
        1.导入进程包 import multiprocessing
        2.通过进程类创建进程对象 obj = multiprocessing.Process(target=任务名)
            target：执行的目标任务名，这里指的是函数名
            name：进程名，一般不用设置
            group：进程组，目前只能使用None
        3.启动进程执行任务 obj.start()
'''

import time
import multiprocessing

# 唱歌
def sing():
    for i in range(3):
        print("唱歌...")
        time.sleep(1)

# 跳舞
def dance():
    for i in range(3):
        print("跳舞...")
        time.sleep(1)


if __name__ == '__main__':
    #创建子进程
    sing_process = multiprocessing.Process(target=sing)
    #创建子进程
    dance_process = multiprocessing.Process(target=dance)
    #启动进程
    sing_process.start()
    dance_process.start()