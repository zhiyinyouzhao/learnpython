
class Company(object):
    def __init__(self,employ_list):
        self.employee = employ_list

    #魔法函数,__开始
    def __getitem__(self, item):
        return self.employee[item]


company = Company(['tom','bob','jane'])

for em in company:
    print(em)

