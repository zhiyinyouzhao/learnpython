
# -*- coding: utf-8 -*-

import sys
import copy
import json
from imp import reload

reload(sys)
sys.setdefaultencoding('utf8')

'''
浅copy: 只拷贝复合对象中的父对象，不拷贝对象内部的子对象。
深copy: 拷贝对象的父对象和子对象。
copy和deepcopy对于不可变对象，比如Str，Int，Tuple，产生的结果都是一样的，都是增加了一个引用，id也是相同的.
但对于不可变对象，是重新创建了个对象，并添加了一个引用，如上面的alist和a，在alist append操作后，你会发现，a中的值还是原先的值，他们的id是不同的，
此处是copy和deepcopy的真正区别，可变对象中嵌套有可变对象，浅拷贝只会复制第一层的元素，对于嵌套的可变对象，仍旧存的是原先的地址，如上图输出，但deepcopy会把嵌套的对象完全拷贝，并开辟一片空间，成为一个新的对象。
'''
# 由于 Python 内部引用计数的特性，对于不可变对象，浅拷贝和深拷贝的作用是一致的，就相当于复制了一份副本，原对象内部的不可变对象的改变，不会影响到复制对象
# 浅拷贝的拷贝。其实是拷贝了原始元素的引用（内存地址），所以当拷贝可变对象时，原对象内可变对象的对应元素的改变，会在复制对象的对应元素上，有所体现
# 深拷贝在遇到可变对象时，又在内部做了新建了一个副本。所以，不管它内部的元素如何变化，都不会影响到原来副本的可变对象
# （1）当对象为不可变类型时，不论是赋值，浅拷贝还是深拷贝，那么改变其中一个值时，另一个都是不会跟着变化的。
# （2）当对象为可变对象时，如果是赋值和浅拷贝，那么改变其中任意一个值，那么另一个会跟着发生变化的；如果是深拷贝，是不会跟着发生改变的。
'''
可变对象包括：list，dict，set
------对象存放在地址中的值不会被改变（所谓的改变是创建了一块新的地址并把新的对象的值放在新地址中原来的对象并没有发生变化）[2]
不可对象包括：数字，字符串，tuple
------对象存放在地址中的值会原地改变
闭包：就是在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且 外函数的返回值是内函数的引用。
装饰器(本质就是闭包)：主要作用为已经存在的对象添加额外的功能，例如日志记录、数据校验等。
'''



DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum


def log1(f):
    def wrapper(*args, **kw):
        print('call %s():' % f.__name__)
        return f(*args, **kw)
    return wrapper


@log1
def now():
    print '2015-3-25'

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' %(self.__name,self.__score)


class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

def run_twice(animal):
    animal.run()

def read():
    try:
        f = open('F:\\test.txt','r')
    finally:
        if f:
            f.close()


def insert_sort(nums):
    for i in range(1,len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and temp < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp
    return nums

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j+1] < nums[j]:
                nums[j+1],nums[j] = nums[j],nums[j+1]
    return nums


def quick_sort(nums,low,high):
    if low < high:
        i = low
        j = high
        key = nums[i]
        while i != j:
            while i < j and nums[j] >= key:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= key:
                i += 1
            nums[j] = nums[i]
        nums[i] = key
        quick_sort(nums,low,i-1)
        quick_sort(nums,i+1,high)
    return nums


def select_sort(nums):
    for i in range(len(nums)-1):
        # 寻找[i,n]区间里的最小值
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums

def selectionSort(alist):
    n = len(alist)
    for i in range(n - 1):
        # 寻找[i,n]区间里的最小值
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


def binary_serach(nums,key):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high)/2
        if nums[mid] == key:
            return mid
        elif nums[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    # with open('F:\\test.txt','w') as f:
    #     f.write('111111')
    nums = [49,38,65,97,76,13,27,49]
    res1 = insert_sort(nums)
    print res1
    res2 = bubble_sort(nums)
    print res2
    res3 = quick_sort(nums,0,len(nums)-1)
    print res3
    res4 = select_sort(nums)
    print res4
    res5 = binary_serach([13,27,38,49,49,65,76,97], 76)
    print res5





