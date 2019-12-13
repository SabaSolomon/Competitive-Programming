from collections import deque

class Stack:
    queue = deque()
    def push(self, num):
        self.queue.append(num)
        for i in range (len(self.queue)):
            x = self.queue.popleft()
            self.queue.append(x)

    def pop(self):
        return (self.queue.pop())
    
stack = Stack()
stack.push(3)
stack.push(5)
print(stack.queue)
print(stack.pop())

print(stack.queue)
