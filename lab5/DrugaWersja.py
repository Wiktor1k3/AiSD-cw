from typing import Any, Callable


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

    def add_left_child(self, value:Any):
        self.left_child = BinaryNode(value)
        self.left_child.parent = self

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)
        self.right_child.parent = self

    def traverse_in_order(self, visit:Callable[['Any'], None]):

        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit:Callable[['Any'], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit:Callable[['Any'], None]):
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

class BinaryTree:
    def __init__(self, root: BinaryNode):
        self.root = root

    def traverse_in_order(self, visit:Callable[['Any'], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit:Callable[['Any'], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit:Callable[['Any'], None]):
        self.root.traverse_pre_order(visit)



    def show(self):
        spacer = " |===|"
        if type(self) is BinaryTree:
            if self.root.left_child:
                BinaryTree.show(self.root.left_child)
            print("|"+str(self.root.value)+"|")
            if self.root.right_child:
                BinaryTree.show(self.root.right_child)
        if type(self) is BinaryNode:
            if self.left_child:
                BinaryTree.show(self.left_child)

            print("  " + spacer*self.level_of()+str(self.value)+"|")
            if self.right_child:
                BinaryTree.show(self.right_child)
def visit(node:BinaryNode):
    print(node.value)




def all_paths(tree:BinaryTree):

    root = tree.root
    paths = [[]]
    path = []
    # przechodzenie deep_first
    queue = []
    queue.append((root, path))
    if root == None:
        raise ValueError("root nie moze byc None")

    while queue:
        node, path = queue[-1]
        del queue[-1]
        path.append(node)
        if node.is_leaf():
            paths.append(list(path))
        if node.right_child:
            queue.append((node.right_child, list(path)))
        if node.left_child:
            queue.append((node.left_child, list(path)))

    return paths


























bn = BinaryNode(10)

bn.add_left_child(9)
bn.add_right_child(2)

bn.left_child.add_left_child(1)
bn.left_child.add_right_child(3)

bn.right_child.add_left_child(4)
bn.right_child.add_right_child(6)

bn.left_child.left_child.add_left_child(5)
bn.left_child.right_child.add_right_child(7)

bn.right_child.left_child.add_right_child(8)
bn.right_child.right_child.add_left_child(0)
bn.right_child.right_child.add_right_child(12)

bn.right_child.right_child.right_child.add_left_child(13)
bn.right_child.right_child.right_child.add_right_child(14)



bt = BinaryTree(bn)


bt.show()
lista = all_paths(bt)
strng = ""
for x in lista:
    print("\n")
    for y in x:
        strng+="[" + str(y.value)+"]"
    print(strng)
    strng = ""
