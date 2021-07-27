

class A:
    name = "A"
    def __init__(self):
        self.name = 'obj'

a = A()
'''
查找顺序由下到上
'''
print(a.name)
