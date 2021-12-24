'''
    什么是对象的成员？
        一个对象通过类实例化后，那么在类中定义的属性和方法，可以使用实例化的对象进行操作。
        类中定义的属性称为成员属性，类中定义的方法，称为成员方法
'''

class Cart():
    color = '白色'
    brand = '奥迪'
    pailiang = 2.4

    def lahuo(self):
        print('小汽车能拉货')

    def doufeng(self):
        print('小汽车能兜风')

    def bamei(self):
        print("带妹子去兜风...")

if __name__ == '__main__':
    a = Cart()
    b = Cart()
    print(a)
    print(b)
    print("===================")
    '''
        以上a和b变量都是对象，都是通过cart类实例化来的对象
        但是a和b是两个对象，相同之处就在于都由同一个类实例化出来
    '''

    # 对象的成员的操作，1.在类的外部，使用对象操作成员
    # 访问成员属性：先访问a对象自己的color属性，没有就去访问这个对象的类的属性
    res = a.color   #通过对象访问类中的属性
    print(res)
    res = a.lahuo() #通过对象访问类中的方法

    # 修改对象的属性值：实际上等于给这个对象创建了一个a对象自己的属性
    a.color = '黑色'  #修改对象的属性
    print(a.color)
    # 此时b对象的color属性是什么？
    print(b.color)  # b对象的属性依旧是原来的值


    #添加对象的属性：给当前a对象创建了自己独有属性
    a.name = 'a6'
    # 此时b对象是否有name这个属性呢？
    #print(b.name)   # 给a添加name属性，此时的name属性只属于a这个对象，b没有这个属性


    # 删除属性，只能删除对象自己的属性，包括给对象添加的和修改的
    del a.color
    # del a.brand     #无法删除brand属性，但是name属性可以删除
    # print(a.brand)
    ''''
        删除一个对象的属性时，只能删除当前这个对象自己的属性才可以
        上面例子中brand这个属性并不是a自己的属性，而是属于cart类
        而name属性是单独给a对象添加的属性，因此可以删除    
    '''

    print("===================")
    # 对象的成员的操作，1.在类的外部，使用对象操作成员
    # 访问对象的方法：实际上如果这个对象没有自己独立的方法，那么会访问这个对象的类方法。
    res = a.lahuo() # 通过对象访问类中方法
    print(res)
    # 修改对象的方法:给这个对象的方法重新定义
    def func():
        print('这是一个新的方法')
    a.lahuo = func
    a.lahuo()
    # 添加新的方法:给对象自己新创建的方法
    a.func2 = func
    a.func2()

    #删除方法：可以删除当前对象自己的方法
    del a.lahuo
    a.lahuo()


