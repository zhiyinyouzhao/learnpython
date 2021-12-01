


#1.使用{}定义
vardict = {'a':1,'b':2,'c':2}

#2. 使用dict(key=value,key=value) 函数进行定义
vardict1 = dict(name='zhangsan',sex='男',age=22)

#3. 数据类型的转换 dict(二级容器类型) 列表或元组，并且是二级容易才可以转换
vardict2 = dict([['a',1],['b',2]])
print(vardict2)

# zip函数


# 字典的操作
var1 = {'a':1,'b':2,'c':3}
var2 = {1:'a',2:'b',3:'c',4:'d'}

#获取元素
res = var1['a']

#修改元素
res= var1['a'] = 111

#删除元素
del var1['a']

#添加元素
var1['aa'] = 'AA'

#如果字典中的key重复了，会被覆盖

#成员检测，只能检测key，不能检测value
res = 'AA' in var1
res1 = 'AA' not in var1

#获取长度，检测当前有多少个键值对
res3 = len(var1)

#获取当前字典中的所有key,values
res4 = var1.keys()
res5 = var1.values()

#获取当前字典中所有的键值对
res6 = var1.items()

#对字典进行遍历
for i in var1:
    print(i)    #在遍历当前的字典时，只能获取当前的key

for k,v in var1.items():
    print(k,v)

for k in var1.keys():
    print(k)

for v in var1.values():
    print(v)