
'''
    线程池：
        1.python3中官方才正式提供线程池。
        2.线程不是开的越多越好，开的多了可能会导致系统的性能更低了。
        3.不建议无限制的创建线程。
'''

import threading
import time
from concurrent.futures import ThreadPoolExecutor

'''
    pool = ThreadPoolExecutor(10)
    pool.submit(函数名，参数1，参数2，.......)
'''

# 创建线程池，最多维护10个线程
pool = ThreadPoolExecutor(10)
url_list = ["www.xxxx-{}".format(i) for i in range(300)]

def task(video_url,num):
    print('开始执行任务',video_url)
    time.sleep(5)




if __name__ == '__main__':
    for url in url_list:
        #在线程池中提交一个任务，线程池如果有空闲线程，则分配一个线程去执行，执行完毕后再将线程交给线程池；如果没有空闲线程，则等待
        pool.submit(task,url,2)
    #for循环会一下全部执行完，300次循环会全部执行完，任务交个线程池
    print("end")
    # 主线程到此停下来，等待子线程
