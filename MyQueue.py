class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def pop(self):
        if self.head != None:
            self.head = self.head.next
        else:
            Exception("Stack is empty")

    def peek(self):
        if self.head != None:
            return self.head
        else:
            Exception("Stack is empty")

    def printQueue(self):
        if self.head != None:
            temp = self.head
            while temp != None:
                print(f"---->{temp.data}")
                temp = temp.next
        else:
            Exception("Stack is empty")

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True


queue = Queue()
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.printQueue()
print(f"head:{queue.peek()}")
queue.pop()
queue.printQueue()
print(f"Is empty? {queue.isEmpty()}")
