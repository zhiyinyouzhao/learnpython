

'''
类属性，实例属性

'''

class A:
    name = "A"
    def __init__(self):
        self.name = 'obj'

a = A()
'''
实例查找顺序：由下到上
'''
print(a.name)

#python3 新式类，写不写都会继承object
class D():
    pass

class C(D):
    pass

class B(D):
    pass

class A(B,C):
    pass

print(A.__mro__)