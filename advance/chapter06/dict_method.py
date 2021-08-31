
a = {"bobby1":{"company":"imooc"},
     "bobby2":{"company":"imooc2"}}

# a.clear()
# print(a)


'''
copy,返回浅拷贝
'''

# new_dict = a.copy()
# new_dict["bobby1"]["compamy"] = "imooc3"
# print(a)


#formkeys 将可迭代对象转为dict
new_list = ["bobby1","bobby2"]
new_dict = dict.fromkeys(new_list,{"company":"imooc"})
print(new_dict)

for k,v in new_dict.items():
     print(k,v)

# default_value = new_dict.setdefault("bobby","imooc")
# print(default_value)
# print(new_dict)

new_dict.update([("bobby","imooc")])
new_dict.update(bobby3="imooc3")
print(new_dict)