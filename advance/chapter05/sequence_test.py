

a = [1,2]
b = list()
c = a+[3,4]

# += 就地加
a += (3,4)
a.extend(range(3))
print(a)