

'''
    局部变量：
        函数内定义的变量，函数外不能使用


    全局变量：
        在函数内部使用global关键字定义的变量就是全局变量，任意位置都可以使用
        在函数外定义的变量，在函数内使用global 关键字进行声明，那么也是全局变量，任意位置都可以使用

    globals()；获取全局数据
    locals(): 获取当前作用域的数据

    变量分2种：
        可变数据类型：在函数外定义的变量，在函数内可以使用
            列表和字典
        不可变数据类型：在函数外定义的变量，在函数内只能访问，不能使用其他操作
'''



num = 10

def func():
    print(num)   #在函数内可以获取函数外部的变量
    # num += 20    #在函数内不能直接更改函数外的变量

    love = 20   #函数能定义的变量，在函数外不能使用
    # global num
    # num += 20
    # print(num)
    global live
    live = 'iliveyou'
    print(globals())
    print(locals())


if __name__ == '__main__':
    func()
    # print(globals())
    # print(locals())