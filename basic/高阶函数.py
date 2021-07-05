

from functools import reduce
'''
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
'''

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
'''

'''
filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''

def f(x):
    return x * x

def add(x,y):
    return x + y

def fn(x,y):
    return x * 10 + y

def is_odd(n):
    return n %2 == 1

if __name__ == '__main__':
    # r = map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])
    # print(list(r))
    # r1 = reduce(add,[1,2,5,7,9])
    # print(r1)
    # r2 = reduce(fn, [1, 3, 5, 7, 9])
    # print(r2)
    r3 = filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15])
    print(list(r3))