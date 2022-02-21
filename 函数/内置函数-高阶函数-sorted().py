

'''
    sorted()
        原理：把可迭代数据里面的元素，一个一个的取出来，放到key这个函数中进行处理，
             并按照函数中return的结果进行排序，返回䘝新的列表
        功能：排序
        参数：iterable 可迭代的对象（容器类型数据，range数据序列，迭代器）
             reverse  可选，是否反转。默认为False，不反转，True反转
             key     可选，函数，可以试自定义函数，也可以是内置函数
        返回值：排序后的结果
'''

#自定义函数
def func(num):
    return num % 2


if __name__ == '__main__':
    arr = [3,7,1,-9,20,10]
    res1 = sorted(arr)
    res2 = sorted(arr,reverse=True)
    res3 = sorted(arr,key=abs)
    print("res1:",res1)
    print("res2:",res2)
    print("res3:",res3)


    arr1 = [3,2,4,6,5,7,9]
    res4 = sorted(arr1,key=func)
    res5 = sorted(arr1,key=lambda x:x%2)
    print("res4:",res4)
    print("res5:",res5)

    print(3%2,2%2,4%2,6%2,5%2,7%2,9%2)