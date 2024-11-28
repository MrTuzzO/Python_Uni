from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError('Stack is empty')

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


st = Stack()

print(st.size())
print(st.is_empty())
st.push(5)
st.push(6)
print(st.peek())

print(st.pop())
st.push(7)
st.push(8)
print(st.size())
print(st.is_empty())