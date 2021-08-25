class Company(object):
    def __init__(self,employ_list):
        self.employee = employ_list

    #字符串格式化调用
    def __str__(self):
        return ",".join(self.employee)

    # 开发模式调用
    def __repr__(self):
        return ",".join(self.employee)
company = Company(['tom','bob','jane'])
print(company)
company