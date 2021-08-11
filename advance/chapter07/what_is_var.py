
#python 和java中的变量本质不一样，python的变量实质上是一个指针 int str，便利贴

a  = 1
#1. a贴在1上面
#2. 先生成对象，然后贴便利贴

a = [1,2,3]
b = a
b.append(4)
# print(id(a),id(b))
# print(a is b)
# print(a)


a = [1,2,3,4]
b = [1,2,3,4]
'''
特殊小整数，小字符串内部优化
'''
# a = 1
# b = 1
print(id(a),id(b))
print(a is b)
print(a == b)