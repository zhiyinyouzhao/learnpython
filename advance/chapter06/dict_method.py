
a = {"bobby1":{"company":"imooc"},
     "bobby2":{"company":"imooc2"}}

#clear
# a.clear()
# print(a)

# formkeys

new_list = ["bobby1","bobby2"]
new_dict = dict.fromkeys(new_list,{"company":"imooc"})
print(new_dict)