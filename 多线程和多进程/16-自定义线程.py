# -*- coding: utf-8 -*-


import threading
import time


class MyThread(threading.Thread):
    def __init__(self,name):
        super(MyThread,self).__init__()
        self.name = name

    def run(self):
        print 'task',self.name
        time.sleep(1)
        print '2s'
        time.sleep(1)
        print '1s'
        time.sleep(1)
        print '0s'
        time.sleep(1)

if __name__ == '__main__':
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()