

import time
import random
from concurrent.futures import ThreadPoolExecutor

'''
    pool = ThreadPoolExecutor(10)
    pool.submit(函数名，参数1，参数2，.......)
'''

# 创建线程池，最多维护10个线程
pool = ThreadPoolExecutor(10)
url_list = ["www.xxxx-{}".format(i) for i in range(15)]

def task(video_url):
    print('开始执行任务',video_url)
    time.sleep(2)
    return random.randint(0,10)

def done(response):
    print("任务执行后的返回值",response.result())




if __name__ == '__main__':
    for url in url_list:
        #在线程池中提交一个任务，线程池如果有空闲线程，则分配一个线程去执行，执行完毕后再将线程交给线程池；如果没有空闲线程，则等待
        #线程池先整体去执行一个任务，任务执行完成后，再执行done函数
        future = pool.submit(task,url)
        future.add_done_callback(done)
    '''
        可以做分工，例如task做下载，done专门讲下载的数据写入本地文件
    '''
