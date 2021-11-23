

'''
语法：
    lambda 【参数列表】：返回值
'''


# 封装一个函数做加法运算
#普通函数
def jia(x,y):
    return x+y

#改成lambda表达式封装
res = lambda x,y:x+y

#带有分支结构的lambda表达式
#lambda 参数列表:真区间 if 表达式 表达式判断 else 假区间
r = lambda sex: "很man" if sex == '男' else "很nice"


if __name__ == '__main__':
    print(jia(2,3))
    print(res(4,4))
    print(r('女'))
