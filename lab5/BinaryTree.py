from typing import Any

class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        if self.left_child or self.right_child != None:
            return False
        return True

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self):
        if self:
            BinaryNode.traverse_in_order(self.left_child)
            print(self.value)
            BinaryNode.traverse_in_order(self.right_child)

    def traverse_post_order(self):
        if self:
            BinaryNode.traverse_post_order(self.left_child)
            BinaryNode.traverse_post_order(self.right_child)
        print(self.value)

    def traverse_pre_order(self):
        print(self.value)
        if self:
            BinaryNode.traverse_pre_order(self.left_child)
            BinaryNode.traverse_pre_order(self.right_child)


class BinaryTree:
    def __init__(self, root: BinaryNode):
        self.root = root

    def traverse_in_order(self):

        if type(self) is BinaryTree:
            if self.root.left_child:
                BinaryTree.traverse_in_order(self.root.left_child)
            print(self.root.value)
            if self.root.right_child:
                BinaryTree.traverse_in_order(self.root.right_child)

        if type(self) is BinaryNode:
            if self.left_child:
                BinaryTree.traverse_in_order(self.left_child)
            print(self.value)
            if self.right_child:
                BinaryTree.traverse_in_order(self.right_child)

    def traverse_post_order(self):

        if type(self) is BinaryTree:
            if self.root.left_child:
                BinaryTree.traverse_post_order(self.root.left_child)
            if self.root.right_child:
                BinaryTree.traverse_post_order(self.root.right_child)
            print(self.root.value)

        if type(self) is BinaryNode:
            if self.left_child:
                BinaryTree.traverse_post_order(self.left_child)
            if self.right_child:
                BinaryTree.traverse_post_order(self.right_child)
            print(self.value)

    def traverse_pre_order(self):

        if type(self) is BinaryNode:
            print(self.value)
            if self.left_child:
                BinaryTree.traverse_pre_order(self.left_child)
            if self.right_child:
                BinaryTree.traverse_pre_order(self.right_child)

        if type(self) is BinaryTree:
            print(self.root.value)
            if self.root.left_child:
                BinaryTree.traverse_pre_order(self.root.left_child)
            if self.root.right_child:
                BinaryTree.traverse_pre_order(self.root.right_child)

# def all_paths(stack, root):
#     if root == None:
#         return
#
#     stack.append(root.value)
#     print(stack)
#     if (root.left_child == None and root.right_child == None):
#         print(' '.join([str(i) for i in stack]))
#
#     all_paths(stack, root.left_child)
#     all_paths(stack, root.right_child)
#     stack.pop()

def all_paths(tree):

    if tree.root == None:
        return

    stack = []
    a = []
    b = []
    stack.append((tree.root, b))

    while stack:
        c, b = stack.pop()
        b.append(c.value)
        if c.is_leaf():
            a.append(b)
        if c.left_child:
            stack.append((c.left_child, list(b)))
        if c.right_child:
            stack.append((c.right_child, list(b)))
    return a[::-1]


bn = BinaryNode(1)

bn.add_left_child(2)
bn.add_right_child(3)

bn.left_child.add_left_child(4)
bn.left_child.add_right_child(5)
bn.right_child.add_right_child(7)

bn.left_child.left_child.add_left_child(8)
bn.left_child.left_child.add_right_child(9)

# bn.traverse_pre_order()
bt = BinaryTree(bn)
# bt.traverse_pre_order()

# print(all_paths(bt))

print(' \n'.join(str(i) for i in all_paths(bt)))
