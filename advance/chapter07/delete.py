
'''
python垃圾回收算法采用引用计数
'''

a = object()
b = a
del a
print(b)
print(a)