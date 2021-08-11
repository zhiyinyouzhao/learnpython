

# 模式[start:end:step]
'''
1.第一个数字start表示切片开始位置，默认为0
2.第二个数字end表示切片截止（但不包含）位置（默认为列表长度）
3.第三个数字step表示切片的步长（默认为1）
4.当start为0时可以省略，当end为列表长度时可以省略
5.当step为1时可以省略，并且省略步长时可以同时省略最后一个冒号
6.step为负数的时候，表示反向切片，这时start应该比end的值要大才行
'''


aList = [3,4,5,6,7,9,11,13,15,17]
print(aList[::])
print(aList[::-1])
print(aList[::2])
print(aList[1::2])
print(aList[3:6])
print(aList[0:100])
print(aList[100:])

aList[len(aList):] = [9] # 在列表尾部添加元素
print(aList)
aList[:0] = [1,2]         # 在列表头部插入元素
print(aList)
aList[3:3] = [4]          # 在列表中间插入元素
print(aList)