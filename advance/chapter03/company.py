
class Company(object):
    def __init__(self,employ_list):
        self.employee = employ_list

    def __getitem__(self, item):
        return self.employee[item]

    # def __len__(self):
    #     return len(self.employee)
'''
#魔法函数,__开始,增强class类型，功能，不属于class，也不是继承与object，独立的存在
不需要显示调用
'''

company = Company(['tom','bob','jane'])
company1 = company[:2]
# 定义了__getitem__方法后，该类实例化出来的对象就是一个可迭代对象
# 循环compay对象时，python解释器就回去调用__getitem__
for em in company:
    print(em)
print(company1)
print(len(company))

