# linked list stack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:  # FILO
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head == None:
            raise Exception("Stack is empty")
        else:
            temp = self.head.data
            self.head = self.head.next
        return temp

    def peek(self):
        if self.head == None:
            raise Exception("Stack is empty")
        else:
            return self.head.data

    def print(self):
        if self.head == None:
            raise Exception("Stack is empty")
        else:
            temp = self.head
            while temp != None:
                print(f"---->: {temp.data}")
                temp = temp.next


stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.print()
popped = stack.pop()
print(f"popped: {popped}")
stack.print()
