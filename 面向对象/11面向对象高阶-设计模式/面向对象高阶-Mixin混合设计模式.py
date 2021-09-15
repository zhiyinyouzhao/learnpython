

'''
Mixin 混合设计模式

'''


#交通工具
class vehicle():
    #运输货物
    def huo(self):
        print('运输货物')

    #搭载乘客
    def ren(self):
        print('搭载乘客')

'''
此时定义一个飞行器的类，让需要飞行的交通工具，直接继承这个类，可以解决该问题
但是：
    1.出现多继承，违背了‘is-a’
    2.飞行器这个类很容易被误解
'''
#飞行器
class Flying():
    def fly(self):
        print('可以起飞了')


#定义汽车
class cart(vehicle):
    pass

#定义飞机
class airplane(vehicle):
    pass

#定义直升机
class helicopter(vehicle):
    pass

