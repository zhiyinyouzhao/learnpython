

class A:
    # aa是类变量
     aa = 1

     def __init__(self,x,y):
         # self是类实例，不是类，x,y就属于实例，而不是类
         self.x = x
         self.y = y


# a = A(2,3)
# print(a.x,a.y,a.aa)
# print(A.aa)
# print(A.x)

a = A(2,3)
A.aa = 11
# 下面这句会把值赋值给a实例的属性aa(新建的aa)
a.aa = 100
print(a.x,a.y,a.aa)
print(A.aa)
print(id(A.aa))
print(id(a.aa))
