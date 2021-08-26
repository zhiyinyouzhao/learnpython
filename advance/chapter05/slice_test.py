

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
print(aList[::])  #返回包含原列表中所有元素的新列表
print(aList[::-1])  #返回包含原列表中所有元素的逆序列表
print(aList[::2])   #隔一个取一个，获取偶数位置的元素
print(aList[1::2])  #隔一个取一个，获取奇数位置的元素
print(aList[3:6])   #指定切片的开始和结束位置
print(aList[0:100]) #切片结束位置大于列表长度时，从列表尾部截断
print(aList[100:])  #切片开始位置大于列表长度时，返回空列表

aList[len(aList):] = [9] # 在列表尾部添加元素
print(aList)
aList[:0] = [1,2]         # 在列表头部插入元素
print(aList)
aList[3:3] = [4]          # 在列表中间插入元素
print(aList)
aList[:3] = [1,2]         # 替换列表元素，等号两边的列表长度相等
print(aList)
aList[3:] = [4,5,6]       # 等号两边的列表长度在可以不相等
print(aList)
aList[::2] = [0] * 3      #隔一个修改一个
print(aList)
aList[::2] = ['a','b','c'] #隔一个修改一个
print(aList)
# aList[::2] = [1,2]         #左侧切片不连续，等号2边列表长度必须相等
aList[:3] = []              #删除列表中前3个元素

del aList[:3]           #连续删除
del aList[::2]          #切片元素不连续，隔一个删一个