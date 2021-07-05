
# -*- coding: utf-8 -*-


'''
1.with 作用和try。。。finally一样的。
2.with原理是上下文管理器。
3.任何实现了__enter__()和__exit__()方法的对象都可以称为上下文管理器。
4.__enter()__返回资源对象，这里就是要打开的文件，__exit__()处理一些清理工作。
'''

class File():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print 'enter...'
        self.f = open(self.filename,self.mode)
        return self.f

    def __exit__(self, *args):
        print 'will exit...'
        self.f.close()

if __name__ == '__main__':
    with File('F:\\test.txt','w') as f:
        print 'writing'
        f.write('hello,python')