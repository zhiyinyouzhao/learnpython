# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

# 先序遍历
# 递归
def preorder(root):
    if not root:
        return
    print root.val
    preorder(root.left)
    preorder(root.right)
# 迭代
def preorder(root):
    if not root:
        return
    s = [root]
    while s:
        current = s.pop()
        print current.val
        if current.right:
            s.append(current.right)
        if current.left:
            s.append(current.left)
# 中序遍历
#递归
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val
    inorder(root.right)


# 迭代
def inorder(root):
    if not root:
        return
    current = root
    s = []
    while current or s:
        while current:
            s.append(current)
            current = current.left
        current = s.pop()
        print current.val
        current = current.right
# 后序遍历：
#递归
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print root.val
#迭代
def postorder(root):
    if not root:
        return
    #//第一个stack用于添加node和它的左右孩子
    s1 = []
    #//第二个stack用于翻转第一个stack输出
    s2 = []
    s1.append(root)
    while s1:
        current = s1.pop()
        s2.append(current)
        #// 把栈顶元素的左孩子和右孩子分别添加入第一个stack
        if current.left:
            s1.append(current.left)
        if current.right:
            s1.append(current.right)
    #遍历输出第二个stack，即为后序遍历
    while s2:
        print s2.pop().val