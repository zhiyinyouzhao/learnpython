

money = 0

# def work():
#     global money
#     money += 100

'''
闭包特点：
    1.在外函数中定义了局部变量，并且在内部函数中使用了这个局部变量
    2.在外函数中返回了内涵数，返回的内涵数就是闭包函数
    3.主要在于保护了外函数中的局部变量，既可以被使用，又不会被破坏

'''

def person():
    money = 0
    print(11111111)
    def work():
        print(222222222)
        nonlocal money      #在内涵数中使用了外函数的临时变量
        money += 100
        print(money)
    print(333333333)
    # 在外函数中返回了内涵数，这个内涵数就是闭包函数
    return work
    # def overtime():
    #     nonlocal money
    #     money += 200
    #
    # def buy():
    #     nonlocal money
    #     money -= 50
    #


if __name__ == '__main__':
    res = person()
    print(4444444444444)
    print(res,type(res))
    res()

# 如何检测一个函数时否为闭包函数?
# 函数名.__closure__,如果是闭包函数返回cell
    print(person.__closure__)
    print(res.__closure__)
