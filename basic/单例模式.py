# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')



# 1.使用模块

# 2.使用装饰器
def singleton(cls):
    # 单下划线的作用是这个变量只能在当前模块里访问,仅仅是一种提示作用
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


@singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x
        print('这是A的类的初始化方法')


if __name__ == '__main__':
    a1 = A(2)
    a2 = A(3)
    print(id(a1), id(a2))
