# -*- coding: utf-8 -*-


import time
import multiprocessing

def work():
    for i in range(10):
        print('工作中...')
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    # 设置守护主进程，主进程结束，子进程会自动销毁，不再执行子进程代码
    work_process.daemon = True
    work_process.start()
    time.sleep(1)
    print('主进程执行完了...')