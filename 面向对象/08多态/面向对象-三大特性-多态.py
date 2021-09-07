


'''
多态：对于同一个方法，由于调用的对象不同（或者传入的对象不同），最终实现了不同的结果

'''


class Computer():
    def usb(self,obj):
        obj.start()

class Mouse():
    def start(self):
        print('鼠标启动成功.....')

class KeyBord():
    def start(self):
        print('键盘启动成功.....')

class Udisk():
    def start(self):
        print('U盘启动成功.....')

if __name__ == '__main__':
    c = Computer()
    m = Mouse()
    k = KeyBord()
    u = Udisk()
    c.usb(m)
    c.usb(k)
