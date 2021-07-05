
import time


def print_odds():
    for i in range(100):
        if i % 2 == 1:
            print(i)

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

if __name__ == '__main__':
    print_odds = count_time_wrapper(print_odds)
    print_odds()
