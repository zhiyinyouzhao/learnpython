# -*- coding: utf-8 -*-


import threading
import time


def work():
    for i in range(10):
        print('子线程工作中...')
        time.sleep(0.2)


if __name__ == '__main__':
   # sub_thread = threading.Thread(target=work)
   # sub_thread.start()
   # time.sleep(1)
   # print('主线程结束了...')
   #总结：主进程会等待所有的子线程执行结束在结束
   #因此主线程结束后，子线程会继续执行，进程会等待所有子线程执行完毕后才结束

   #主线程结束不想等待子线程结束而结束，可以设置子线程守护主线程
   sub_thread = threading.Thread(target=work,daemon=True)
   sub_thread.start()
   time.sleep(1)
   print('主线程结束了...')

   # sub_thread = threading.Thread(target=work)
   # sub_thread.setDaemon(True)
   # sub_thread.start()
   # time.sleep(1)
   # print '主线程结束了...'

