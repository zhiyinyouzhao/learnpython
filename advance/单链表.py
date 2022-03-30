
# is_empty() 链表是否为空
# travel()  遍历链表
# length() 链表长度
# items() 获取链表数据迭代器
# add(item) 链表头部添加元素
# append(item) 链表尾部添加元素
# insert(pos, item) 指定位置添加元素
# remove(item) 删除节点
# find(item) 查找节点是否存在


class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self._head = node

    '''链表是否为空'''
    def is_empty(self):
        return self._head is None

    '''链表长度'''
    def length(self):
        # cur游标，用来移动遍历节点
        current = self._head
        # 计数器,记录数量
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return current

    '''遍历'''
    def travel(self):
        current = self._head
        while current is not None:
            print(current.elem)
            current = current.next

    '''链表头部添加元素'''
    def add(self,item):
        node = Node(item)
        # 新结点指针指向原头部结点
        node.next = self._head
        # 头部结点指针修改为新结点
        self._head = node

    """链表尾部添加元素"""
    def append(self,item):
        node = Node(item)
        current = self._head
        if self.is_empty():
            self._head = node
        else:
            while current.next is not None:
                current = current.next
            current.next = node

    '''指定位置添加元素'''
    def insert(self,position,item):
        node = Node(item)
        # position 从0开始
        if position <= 0:
            self.add(item)
        elif position > self.length()-1:
            self.append(item)
        else:
            index = 0
            current =  self._head
            while index < position -1:
                current = current.next
                index += 1
            node.next = current.next
            current.next = node

    '''find(item) 查找节点是否存在'''
    def find(self,item):
        current = self._head
        while current is not None:
            if current.item == item:
                return True
            current = current.next
        return False

    """删除节点"""
    def remove(self,item):
        pre, current = None, self._head
        while current is not None:
            if current.item != item:
                pre = current
                current = current.next
            else:
                #头结点
                if current == self._head:
                    self._head = current.next
                else:
                    pre.next = current.next
                break


if __name__ == '__main__':
    a = [1,2,3,4]
    b = [4,2,3,1]
    print(a==b)
    long 


        







