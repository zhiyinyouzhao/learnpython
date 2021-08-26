
class Group:
    #支持切片操作
    def __init__(self,group_name,company_name,staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self,item):
        return self.staffs[item]

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


if __name__ == '__main__':
    staffs = ["bobby1","imoc","bobby2","bobby3"]
    group = Group(company_name="imooc",group_name="user",staffs=staffs)
    sub_group = group[:2] #item传入slice
    group[0]                #item传入int
    print(len(group))
    reversed(group)