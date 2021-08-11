#set 集合fronzenset（不可变集合）无序;不重复

# s = set('abcde')
# print(s)

s = {'a','b'}
s.add('c')
# print(s)

# s = frozenset("abcde") #frozenset不可变，可以作为dict的key
# print(s)
#向set添加数据
another_set = set("cef")
re_set = s.difference(another_set)
re_set1 = s-another_set
re_set2 = s & another_set
re_set3 = s | another_set
print(re_set)
print(re_set1)
print(re_set2)
print(re_set3)

# / & - 集合运算