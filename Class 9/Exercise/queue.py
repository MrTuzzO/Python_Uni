from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft()


q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)

print(q.dequeue())
print(q.dequeue())