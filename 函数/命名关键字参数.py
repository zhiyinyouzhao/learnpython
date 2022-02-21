



#命名关键字参数

'''
1.关键字参数定义在收集参数后面
2.调用时关键字参数必须通过形参的名字来传递
3.和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
4.如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
5.命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错


'''

def love(a,b,c=3,*args,name):
    print(a,b,c)
    print(args)
    print(name)


#love(1,2,3,4,5,6,7,8,9,name='admin')

def person(name,age,*,city,job):
    print(name,age,city,job)


def person1(name,age,*args,city,job):
    print(name,age,args,city,job)





person('jack',24,city="Beijing",job="Engineer")

# person1('jack',24,city="Beijing",job="Engineer")
#
# person1('jack',24,8,7,city="Beijing",job="Engineer")

