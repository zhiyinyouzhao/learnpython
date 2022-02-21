


def love(a,b,c=3,*args,name,age,**kwargs):
    print(a,b,c)
    print(args)
    print(name,age)
    print(kwargs)       #关键字参数收集，会把多余的关键字参数收集为字典


love(1,2,3,112,123,name='aaa',age=222,sex='ccc',aa='aa',bb='bb')
print("===========================")
love(1,2,3,112,123,age=222,name='aaa',sex='ccc',aa='aa',bb='bb')
print("----------------------")


#注意形参声明的位置
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。