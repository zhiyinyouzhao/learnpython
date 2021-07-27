

class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b,B))
print(isinstance(b,A))

'''
is 判断id是否相同
== 判断值是否相同
'''
print(type(b) is B)
print(type(b) is A)

