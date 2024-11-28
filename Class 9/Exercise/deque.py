from collections import deque

stack = deque()
stack.append(10)
stack.append(20)
print(stack.pop())
print(stack[-1])