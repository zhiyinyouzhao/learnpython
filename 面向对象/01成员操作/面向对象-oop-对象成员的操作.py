

'''
类中定义的属性称为成员属性，类中定义的方法，称为成员方法
'''



class Cart():
    color = '白色'



if __name__ == '__main__':
    a = Cart()
    b = Cart()
    #a 修改了color属性
    a.color = '黑色'
    print(a.color)
    # b对象的属性依旧是原来的值
    print(b.color)
    # 给a添加name属性，此时的name属性只属于a这个对象，b没有这个属性
    a.name = 'a6'
    print(b.name)
