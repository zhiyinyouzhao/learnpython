# -*- coding: utf-8 -*-


'''
    线程：
        1.线程是程序执行的最小单位。
        2.一个进程至少有一个线程来负责执行程序。
        3.线程可与同属一个进程的其他线程共享进程所拥有的的全部资源。

    创建线程：
        1.导入线程模块 import threading
        2.通过线程类创建线程对象 obj = threading.Thread(target=任务名)
        3.启动线程执行任务 obj.start()
'''

import threading
import time
def sing():
    for i in range(3):
        print('唱歌...')
        time.sleep(1)

def dance():
    for i in range(3):
        print('跳舞...')
        time.sleep(1)

if __name__ == '__main__':
   sing_thread = threading.Thread(target=sing)
   dance_thread = threading.Thread(target=dance)

   sing_thread.start()
   dance_thread.start()