

'''
要求：学员的分数在0-100之间
解决方案：
    1.在init方法中检测分数范围
        这个解决方案只能在对象初始化时有效

    2.定义setattr魔术方法检测
        a，加入学员的分数不止一个时怎么办？
        b.另外就是当前类的中的代码是否就比较多了？
    3.可以考虑描述符
'''


# class Student():
#     def __init__(self,id,name,score):
#         print('enter init...')
#         self.id = id
#         print('1111111')
#         self.name = name
#         print('222222')
#         self.score = score
#         print('3333333333')
#
#
#     def returnMe(self):
#         return f'''
#         学员编号:{self.id}
#         学员姓名:{self.name}
#         学员分数:{self.score}
#         '''
#
#     def __setattr__(self, key, value):
#         print('enter __setattr__...........')
#         if key == 'score':
#             if value >= 0 and value <= 100:
#                 object.__setattr__(self,key,value)
#             else:
#                 print('当前分数不符合要求')
#         else:
#             object.__setattr__(self,key,value)

#定义描述符类，代理分数的管理
class Score():
    __score = 0



#使用描述符类代理score分数属性
class Student():
    score = Score()

    def __init__(self,id,name,score):
        print('enter init...')
        self.id = id
        print('1111111')
        self.name = name
        print('222222')
        self.score = score
        print('3333333333')


    def returnMe(self):
        return f'''
        学员编号:{self.id}
        学员姓名:{self.name}
        学员分数:{self.score}
        '''




if __name__ == '__main__':
    zs = Student(1011,'张三丰',99)
    zs.score = -20
    print(zs.score)