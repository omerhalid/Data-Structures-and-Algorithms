class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def pop(self):
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
            return data

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            return None

    def printStack(self):
        if self.head == None:
            print("Stack is empty")
        if self.head.next == None:
            print(self.head)
        temp = self.head
        while temp != None:
            print(f"-----> {temp.data}")
            temp = temp.next


stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.printStack()
print(f"head:{stack.peek()}")
stack.pop()
stack.printStack()
