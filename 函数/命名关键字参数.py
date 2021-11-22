



#命名关键字参数

'''
1.关键字参数定义在收集参数后面
2.调用时关键字参数必须通过形参的名字来传递

'''

def love(a,b,c=3,*args,name):
    print(a,b,c)
    print(args)
    print(name)


love(1,2,3,4,5,6,7,8,9,name='admin')
