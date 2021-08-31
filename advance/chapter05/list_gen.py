

#列表生成式（列表推导式）,性能高于列表操作


#1.提取出1-20之间的奇数
# odd_list = []
# for i in range(21):
#     if i%2==1:
#         odd_list.append(i)

# print(odd_list)

#生成器表达式
o_gen = (i for i in range(21) if i%2 ==1)
print(type(o_gen))
print(o_gen)
for j in o_gen:
    print(j)

o_list = list(o_gen)



# 逻辑复杂的情况
def handle_item(item):
    return item*item
odd_list = [handle_item(i) for i in range(21) if i%2 ==1]
print(odd_list)


#字典推导式
my_dict = {"bobby1":22,"bobby2":23,"imooc.com":5}
reversed_dict = {v:k for k,v in my_dict.items()}
print(reversed_dict)


#集合推导式
my_set = {k for k,v in my_dict.items()}
print(type(my_set))
print(my_set)