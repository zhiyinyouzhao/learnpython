
'''
    p.start()   当前进程准备就绪，等待被CPU调度（工作单元其实是进程中的线程）
    p.join()    等待当前进程的任务执行完毕后再向下继续执行
    p.daemon = 布尔值，守护进程，必须放在start之前
                True    设置为守护进程，主进程执行完毕后，子进程也自动关闭
                False   设置为非守护进程，主进程等待子进程，子进程执行完毕后，主进程才结束
'''


#自定义进程类

import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self):
        print('执行此进程',self._args)

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    p = MyProcess(args=('xxx',))
    p.start()
    print('继续执行...')