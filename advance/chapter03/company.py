class Company(object):
    def __init__(self,employ_list):
        self.employee = employ_list

    def __str__(self):
        return ",".join(self.employee)


company = Company(['tom','bob','jane'])
print(company)