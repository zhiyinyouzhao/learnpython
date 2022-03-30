


import time

class writeLog():
    fileurl = './'
    filename ='2019-09-19'

    #初始化，打开文件
    def __init__(self):
        self.fileobj = open(self.fileurl+self.filename,'a+',encoding='utf-8')

    def log(self,s):
        print('正在写入:%s' %s)

    #析构方法
    def __del__(self):
        print('析构方法触发了')
        # 在对象被销毁时，关闭在初始化方法中打开的文件对象
        self.fileobj.close()


if __name__ == '__main__':
<<<<<<< HEAD
    # 1.
=======
    #1.
>>>>>>> cf93a1682ccf85a8fa07071a1cb416361b68df67
    l = writeLog()
    l.log("今天天气还不错")
    print(',,,,,,,,,,,')

    #2
    # l = writeLog()
    # del l

    pass

