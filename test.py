class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def count(self):
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next

        return count

    def add_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current = self.head
        while current:
            print(f"----> {current.data}")
            current = current.next

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def insert_list(self, testList):
        self.head = None
        for node in testList:
            self.insert_end(node)

    def delete_head(self):
        if self.head != None:
            self.head = self.head.next

    def remove_at(self, index):
        if index == 0:
            self.delete_head()
        else:
            temp = self.head
            for _ in range(index - 1):
                if temp is None:
                    return
                temp = temp.next
            if temp.next is None:
                return
            temp.next = temp.next.next

    def insert_at(self, data, index):
        new_node = Node(data)
        if index == 0:
            self.add_beginning(data)
        else:
            temp = self.head
            for _ in range(index - 1):
                if temp is None:
                    return
                temp = temp.next
            if temp.next is None:
                return
            new_node.next = temp.next
            temp.next = new_node


testList = ["omer", "hale", "ali", "fatma", "ankara"]

linkedList = LinkedList()

linkedList.insert_list(testList)

linkedList.print()
print(f"The count: {linkedList.count()}")
linkedList.delete_head()

print("--------------")
linkedList.print()
print(f"The count: {linkedList.count()}")
print("------------------")
linkedList.remove_at(1)
linkedList.print()
print("Insert index at 2\n")
linkedList.insert_at("INSERTED", 2)
linkedList.print()
