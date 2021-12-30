from typing import Any, Callable


def visit(node:'BinaryNode'):
    return node


class BinaryNode:
    def __init__(self, value:Any):
        self.value = value
        self.left_child: BinaryNode = None
        self.right_child: BinaryNode = None
        self.parent: BinaryNode = None

    def __str__(self):
        return str(self.value)

    def level_of(self):
        lvl = 0
        parent = self.parent
        while parent != None:
            lvl += 1
            parent = parent.parent

        return lvl

    def is_leaf(self):
        if self.left_child or self.right_child:
            return False
        return True

    def min(self):
        if not self.left_child :
            return self
        self.left_child.min()

    def max(self):
        if not self.right_child:
            return self
        self.right_child.max()


    def traverse_in_order(self, visit:Callable[['Any'], 'BinaryNode']):

        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)


class BinarySearchTree:
    def __init__(self, root: BinaryNode):
        self.root = root


    def __insert(self, node:BinaryNode, value:Any):
        if self(type) is BinarySearchTree:
            root = self.root
