

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
解决方案：
    使用多继承，但是给飞行器这个类，定义成为一个Mixin混合类
此时就是等于把飞行器这个类，作为了一个扩展的功能，来扩展其他类
'''
#飞行器
class FlyingMixin():
    def fly(self):
        print('可以起飞了')


#定义汽车
class cart(vehicle):
    pass

#定义飞机
class airplane(vehicle,FlyingMixin):
    pass

#定义直升机
class helicopter(vehicle,FlyingMixin):
    pass

'''
在上面的代码中，虽然直升机和飞机都使用了多继承，也就是继承了FlyingMixin
但是由于FlyingMixin类增加这个名，就告诉了后面阅读代码的人，这个类是一个Mixin类

Mixin表示混入（mix-in）
    Mixin表示一种功能，而不是一个对象
    Mixin的功能必须单一，如果有多个功能，那就多定义Mixin类
    Python中的Mixin是通过多继承实现的，
    Mixin不单独使用，而是混合到其他类中去增加功能的
    Mixin不依赖子类的实现，即便子类没有继承Mixin，子类也能正常运行，可能就是缺少了一些功能
使用Mixin混入类的好处？
    1.在不对类的内容修改的前提下，扩展了类的功能
    2.混入类提高了代码的重用性，使得代码结构简单清晰
    3.可以根据开发需求任意调整（创建新的Mixin混入类）
    4.避免设计多层次的复杂继承关系
'''
