

import time
from concurrent.futures import ThreadPoolExecutor

'''
    pool = ThreadPoolExecutor(10)
    pool.submit(函数名，参数1，参数2，.......)
'''

# 创建线程池，最多维护10个线程
pool = ThreadPoolExecutor(10)
url_list = ["www.xxxx-{}".format(i) for i in range(300)]

def task(video_url):
    print('开始执行任务',video_url)
    time.sleep(5)




if __name__ == '__main__':
    for url in url_list:
        #在线程池中提交一个任务，线程池如果有空闲线程，则分配一个线程去执行，执行完毕后再将线程交给线程池；如果没有空闲线程，则等待
        pool.submit(task,url)
    print("执行中...")
    pool.shutdown(True)     #等待线程池中的任务执行完毕后，再继续执行
    print("继续往下走")
