
'''
    冰冻集合
        语法：只能使用frozenset()函数进行定义
        1.一旦定义不嫩修改
        2.只能做集合相关的运算：求交集，差集...
        3.frozenset()本身就是一个强制转换类的函数，可以把其他任何容器类型数据转为冰冻集合
'''

vars = frozenset({8,1,2,3})
print(vars)

# 遍历
for i in vars:
    print(i)
print(vars)

