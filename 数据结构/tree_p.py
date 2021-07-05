

class TreeNode(object):

    def __init__(self,x):
        self.x = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,x):
        node = TreeNode(x)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = node
                return
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = node
                return
            else:
                queue.append(current.right)

    #'层次遍历'
    def breadth_travel(self):
        if self.root is None:
            return
        #'头结点入队列'
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            # 访问头结点
            print(current.x)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    # 先序遍历
    # 递归
    def preorder(self,root):
        if root is None:
            return
        print(root.x,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    # 循环
    def preorder1(self,root):
        if root is None:
            return
        quque = [self.root]
        while quque:
            current = quque.pop()
            print(current.x, end=" ")
            if current.right is not None:
                quque.append(current.right)
            if current.left is not None:
                quque.append(current.left)

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.x, end=" ")
        self.inorder(root.right)

    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.x,end= " ")


if __name__ == '__main__':
    t = Tree()
    t.add('A')
    t.add('B')
    t.add('C')
    t.add('D')
    t.add('E')
    t.breadth_travel()
    print(" ")
    print(t.root.x)
    t.preorder(t.root)
    print(" ")
    t.inorder(t.root)
    print(" ")
    t.posrorder(t.root)
 