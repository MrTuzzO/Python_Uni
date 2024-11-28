class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Dequeue from an empty queue")
        return self.stack2.pop()

    def is_empty(self):
        return not self.stack1 and not self.stack2


queue = QueueUsingTwoStacks()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.dequeue())


print(queue.is_empty())


print(queue.dequeue())


print(queue.is_empty())
