class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s" % self.data


class LinkedList:
    """Singly Linked List"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """Returns the number of the nodes in the linked list takes 0(n) time"""
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds new node at head of the list
        Takes O(1) time which is our best case scenerio
        :param data:
        :return:
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        :return:
        """

        nodes =[]
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head is %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tails is %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)
    


l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(3)
print(l1.size())
print(l1)
