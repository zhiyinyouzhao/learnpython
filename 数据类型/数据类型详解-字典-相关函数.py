

# len(dict)
# dict.keys()
# dict.values()
# dict.items()

#iter(dict)  #返回以字典的键为元素的迭代器
vardict = {'a':1,'b':2,'c':2}
res = iter(vardict)
print(res,next(res))

#dict.pop(key) #通过key，从当前字典中弹出键值对删除
res1 = vardict.pop('a')
print(res1)
print(vardict)

#dict.get(key),使用get获取不存在的key，不会报错，不存在默认返回Key
res2 =vardict.get('aa')

#dict.setdefault(key,[default]) 如果存在key，返回其值，如果不存在，插入值为default的键key，并返回default。defalut默认值为None。
