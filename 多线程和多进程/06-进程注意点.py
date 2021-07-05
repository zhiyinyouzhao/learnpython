# -*- coding: utf-8 -*-


import time
import multiprocessing

def work():
    for i in range(10):
        print '工作中...'
        time.sleep(0.2)


if __name__ == '__main__':
    # 总结：主进程会等待是所有的子进程执行完毕后退出
    work_process = multiprocessing.Process(target=work)
    work_process.start()
    time.sleep(1)
    print '主进程执行完了...'