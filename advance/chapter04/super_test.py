
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

from threading import  Thread
class MyThread(Thread):
    def __init__(self,name,user):
        self.user = user
        super().__init__(name=name)
# 1.既然我们重写B的构造函数，为什么还要去调用super？
#
# 2.super到底执行顺序使什么样的？ mro顺序
if __name__ == '__main__':
    b = B()