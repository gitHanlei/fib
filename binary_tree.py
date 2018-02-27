# coding utf-8

"""
二叉树的定义和python代码实现

二叉树特点： 1 每个节点的度为2
            2 第i层最多有2**(i-1)个节点
            3 深度为K的树最多有2**k-1个节点
满二叉树： 深度为k， 节点数为2**k-1
完全二叉树: 深度为k，除k层外，所有成的节点数达到最大

二叉树的4种遍历  前序： 根左右，  中序： 左根右，  后序： 左右根, 层次遍历
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while 1:
                pop_node = q.pop(0)

                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def traverse(self):
        """
        按照层次遍历二叉树
        :return:
        """
        if self.root is None:
            return None

        q = [self.root]

        res = [self.root.item]

        while q:
            pop_node = q.pop(0)

            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.item)

            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.item)
        return res

    def pre_first(self, root):
        if root is None:
            return []
        res = [root.item]
        left_item = self.pre_first(root.left)
        right_item = self.pre_first(root.right)
        return res + left_item + right_item

    def middle_first(self, root):
        if root is None:
            return []
        res = [root.item]
        left_item = self.middle_first(root.left)
        right_item = self.middle_first(root.right)
        return left_item + res + right_item

    def after_first(self, root):
        if root is None:
            return []
        res = [self.root.item]
        left_item = self.after_first(root.left)
        right_item = self.after_first(root.right)
        return left_item + right_item + res


t = Tree()

for index in range(10):
    t.add(index)
