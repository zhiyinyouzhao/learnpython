
#多态 继承版

'''
定义一个接口规范类，其他类都继承这个类，并实现重写父类中的方法
由于每个对象实现父类方法的方式或者过程都不相同，最后的结果是不一样的形态
'''


class USB():
    '''
    当前类的说明：
    这个类是一个接口规范类，需要子类继承并实现start方法
    start方法不做任何具体功能的实现
    '''
    def start(self):
        pass

class Mouse(USB):
    def start(self):
        print('鼠标启动成功.....')

class KeyBord(USB):
    def start(self):
        print('键盘启动成功.....')

class Udisk(USB):
    def start(self):
        print('U盘启动成功.....')

if __name__ == '__main__':
    m = Mouse()
    k = KeyBord()
    u = Udisk()

    m.start()
    k.start()
    u.start()

