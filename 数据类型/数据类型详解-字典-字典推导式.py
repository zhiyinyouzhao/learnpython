

# 把字典中的键值对位置进行交换
vardict = {'a':1,'b':2,'c':3}


newdict = {v:k for k,v in vardict.items()}
print(newdict)


# 注意以下推导式，返回的结果是一个集合，集合推导式
newdict1 = {v for k,v in vardict.items()}
print(newdict1,type(newdict1))

# 把以下字典中的是偶数的值，保留下来，并且交换键值对的位置

vardict1 = {'a':1,'b':2,'c':3,'d':4}

newdict2 = {v:k for k,v in vardict1.items() if v%2 == 0}
print(newdict2)