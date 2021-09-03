import time


class Mylog():
    fileurl = './'
    filename = str(time.strftime("%Y-%m-%d"))+'.log'
    fileobj = None



    def __init__(self,):
        self.fileobj = open(self.fileurl+self.filename,'a+',encoding='utf-8')

    def wlog(self,s):
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        msg = date+' '+s+'\n'
        self.fileobj.write(msg)

    def __del__(self):
        self.fileobj.close()



if __name__ == '__main__':
    w = Mylog()
    w.wlog('今天天气不太好')
    w.wlog('所以不出门')
