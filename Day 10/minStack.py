class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if(len(self.stack)==0):
            return 
        self.stack.pop()

    def top(self):
        if(len(self.stack)==0):
            return None
        return self.stack[len(stack)-1]

    def getMin(self):
        if(len(self.stack)==0):
            return None
        min = self.stack[0]
        for i in self.stack:
            if(i<min):
                min = i
        return min

s1 = MinStack()
s1.push(1)
s1.push(9)
s1.push(1)
s1.push(2)
print(s1.stack)
s1.pop()
print(s1.stack)
print(s1.top())
print(s1.getMin())
s2= MinStack()
s2.pop()
print(s2.top())
