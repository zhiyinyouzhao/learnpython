class A():
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    name = '张三'
    age = 33


if __name__ == '__main__':
    res = issubclass(D,B)       #True
    print(res)
    d = D()
    res1 = isinstance(d,D)      #True
    print(res1)
    res2 = hasattr(D,'name')    #True
    print(res2)
    res3 = getattr(d,'name')    #张三
    print(res3)
    res4 =setattr(d,'name','ooo')
    print(d.name)
    res5 = delattr(D,'age')
    print(res5)