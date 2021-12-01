

# 集合基本操作和常规函数


# 集合1.无序，2.布尔类型和0,1只能存在于一个,3.元组值不重复
vars = {1,2,3,'abc','love',True,(1,2,3),False,0,3.1415,123}
print(vars)

# 检测集合中的值
res = '123' in vars

# 获取元素个数len()

# 遍历
for i in vars:
    print(i)

# 添加元素，返回None
# res1 = vars.add('def')
# print(res1)
# # 删除元素，并返回,随机删除
# res2 = vars.pop()
# res3 = vars.pop()
# print(res2)
# print(res3)
# # 删除指定元素,返回None，不存在则报错
# res4 = vars.remove('abc')
# # 删除指定元素，不存在也不报错
# res5 = vars.discard('abc')
# # clear(),清空集合
# res6 = vars.clear()

#update(),返回None
res7 = vars.update({1,2,3,4,5})
print(res7)

'''
    当前集合中浅拷贝不存在深拷贝的问题
    因为集合中的元素都不可变，包括元组和冰冻集合
    不存在拷贝后，对集合中不可变的二级容器进行操作
'''