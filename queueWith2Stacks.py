# The enqueue method simply pushes elements onto the enqueueStack.
# The dequeue method first checks if the dequeueStack is empty. 
# If it is, it pops all elements from enqueueStack and pushes them onto dequeueStack, reversing their order. 
# Then it pops and returns the top element from dequeueStack.

class QueueWithTwoStacks:
    def __init__(self):
        self.enqueueStack = []
        self.dequeueStack = []

    def enqueue(self, item):
        self.enqueueStack.append(item)

    def dequeue(self):
        if not self.dequeueStack:
            while self.enqueueStack:
                self.dequeueStack.append(self.enqueueStack.pop())
        return self.dequeueStack.pop() if self.dequeueStack else None
