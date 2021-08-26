
a = [1,2]
c = a+[3,4]
print(c)

#+= 就地加
a += (3,4)
a.extend(range(3))
print(a)