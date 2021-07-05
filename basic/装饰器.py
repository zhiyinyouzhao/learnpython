
import time


'''
通过装饰器进行函数增强，只是一种语法糖，本质上与闭包程序完全一致
1.增强实际？在第一次调用之前
2.增强次数？只增强一次
'''

'''
语法糖指计算机语言中添加的某种语法，这种语法对于功能没有影响，更方便程序员使用
'''

def count_time_wrapper(func):
    '''
    闭包本质上是一个函数，闭包函数的传入参数和返回值也是函数
    闭包函数的返回值是对传入函数进行增强后的结果
    '''

    def improved_func():
        start_time = time.perf_counter()    # 起始时间
        func()                              # 执行函数
        end_time = time.perf_counter()      # 结束时间
        print('it takes {} s to find the olds'.format(end_time - start_time))
    return improved_func

@count_time_wrapper
def print_odds():
    for i in range(100):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    # 装饰器等价于在第一次调用函数时执行以下语句：
    # print_odds = count_time_wrapper(print_odds)
    print_odds()
