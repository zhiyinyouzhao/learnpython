class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


# is_empty() 链表是否为空
# length() 链表长度
# items() 获取链表数据迭代器
# add(item) 链表头部添加元素
# append(item) 链表尾部添加元素
# insert(pos, item) 指定位置添加元素
# remove(item) 删除节点
# find(item) 查找节点是否存在


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self._head = node

    """判断链表是否为空"""

    def is_empty(self):
        return self._head is None

    """长度"""
    def length(self):
        # cur游标，用来移动遍历节点
        cur = self._head
        # count 记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    """遍历"""
    def travel(self):
        # cur游标，用来移动遍历节点
        cur = self._head
        # count 记录数量
        while cur is not None:
            print(cur.elem)
            cur = cur.next

    """链表头部添加元素"""
    def add(self,item):
        node = Node(item)
        # 新结点指针指向原头部结点
        node.next = self._head
        # 头部结点指针修改为新结点
        self._head = node

    """链表尾部添加元素"""
    def append(self,item):
        node = Node(item)
        cur = self._head
        if self.is_empty():
            self._head = node
        else:
            while cur.next is  not None:
                cur = cur.next
            cur.next = node

    """指定位置添加元素"""
    def insert(self, pos, item):
        #pos 从0开始
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            index = 0
            pre = self._head
            while index < pos -1:
                pre = pre.next
                index += 1
            # 当循环退出后，pre指向pos-1
            node.next = pre.next
            pre.next = node

    "查找节点是否存在"
    def find(self,item):
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    """删除节点"""
    def remove(self,item):
        pre,cur = None,self._head
        while cur is not None:
            if cur.elem == item:
                # 头结点
                if cur == self._head:
                    self._head = cur.next
                else:
                     pre.next == cur.next
                break
            else:
                pre = cur
                cur = cur.next

if __name__ == '__main__':
    link_list = SingleLinkList()
    print(link_list.is_empty())
    print(link_list.length())
    print("======")
    link_list.append(1)
    link_list.append(2)
    link_list.append(3)
    link_list.append(4)
    link_list.append(5)
    link_list.append(6)
    link_list.travel()

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 分割链表
        mid = self.split_linkList(head)
        print mid
        # 反转链表
        reverse_endHalf_head = self.reverse_linkList(mid)
        print reverse_endHalf_head
        # 比较链表
        result = self.compare(head,reverse_endHalf_head)
        return result

    def split_linkList(self,head):
        fast,slow = head,head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_linkList(self,head):
        pre,cur = None,head
        while cur is not None:
            back = cur.next
            cur.next = pre
            pre = cur
            cur = back
        return pre

    def compare(self,headA,headB):
        curA,curB = headA,headB
        while curB is not None:
            if curA.val != curB.val:
                return False
            curA = curA.next
            curB = curB.next
        return True

ListNode{val: 2, next: ListNode{val: 1, next: None}}
ListNode{val: 1, next: ListNode{val: 2, next: None}}

ListNode{val: 2, next: ListNode{val: 1, next: None}}
ListNode{val: 1, next: ListNode{val: 2, next: None}}

ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 2, next: None}}}
ListNode{val: 1, next: ListNode{val: 2, next: None}}

ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 2, next: None}}}
ListNode{val: 1, next: ListNode{val: 2, next: None}}
