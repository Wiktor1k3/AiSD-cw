from typing import Any

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        napis = ""
        while node is not None:
            if node.next != None:
                napis += str(node.value)+" -> "
            if node.next == None:
                napis += str(node.value)
            node = node.next
        return napis

    def __len__(self):
        temp = self.head
        count = 0
        while temp!=None:
            count += 1
            temp = temp.next
        return count

    def push(self,  value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def node(self, at: int) -> Node:
        if len(self) >= at:
            node = self.head
            for x in range(at):
                node = node.next
            return node

    def insert(self, value: Any, after: Node):
        if after is None:
            print("Podano złe dane")
            return
        NewNode = Node(value)
        NewNode.next = after.next
        after.next = NewNode

    def pop(self)->Any:
        node = self.head
        self.head = node.next
        return node

    def remove_last(self) -> Any:
        node = self.head
        for x in range(len(self)-2):
            node = node.next
        node.next = None
        return node

    def remove(self, after: Node) -> Any:
        node = self.head
        if after is None:
            print("Podano złe dane")
            return
        while node != after:
            node = node.next
        node = node.next
        after.next = node.next

    def printLL(self):
        a = self.head
        while(a):
            print(a.value)
            a = a.next

class Stack:
    def __init__(self):
       self.head = None

    def __len__(self):
        temp = self.head
        count = 0
        while temp!=None:
            count += 1
            temp = temp.next
        return count

    def __repr__(self):
        node = self.head
        napis = []
        napis2 =""
        a = len(self)
        while node != None:
            napis.append(node.value)
            node = node.next
        for x in range(a):
            if(x==a-1):
                napis2 += "|" + str(napis[a-x-1]) + "|"
            else:
                napis2+="|"+str(napis[a-x-1])+"|\n"
        return napis2

    def push(self, element: Any) -> None:
        if self.head == None:
            self.head = Node(element)
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = Node(element)

    def pop(self):
        if self.head == None:
            return None
        else:
            node = self.head
            for x in range(len(self)-2):
                node = node.next
            node.next = None

class Queue:
    def __init__(self):
       self.head = None

    def __len__(self):
        temp = self.head
        count = 0
        while temp!=None:
            count += 1
            temp = temp.next
        return count

    def __repr__(self):
        node = self.head
        napis = ""
        while node is not None:
            if node.next != None:
                napis += str(node.value) + ", "
            if node.next == None:
                napis += str(node.value)
            node = node.next
        return napis

    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head

    def enqueue(self, element: Any) -> None:
        if self.head == None:
            self.head = Node(element)
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = Node(element)

    def dequeue(self) -> Any:
        node = self.head
        self.head = node.next
        return node

print("-------Node---------")
LL = LinkedList()

LL.push(3)
LL.push(0)
LL.append("Wiko")
LL.append("Weo")
LL.append("e")
LL.append("w")
LL.append("b")
LL.pop()
LL.insert(2,LL.node(4))
LL.remove_last()
LL.remove(LL.node(4))
print(LL)
print(len(LL))

print("-------Stack---------")
stack = Stack()
assert len(stack) == 0
stack.push(3)
stack.push(2)
stack.push(6)
stack.pop()

print(stack)
print(len(stack))

print("-------Queue---------")
queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'
queue.dequeue()

print(queue)
print(len(queue))
