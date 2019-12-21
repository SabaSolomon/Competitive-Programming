class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        if(len(self.min)==0):
            self.min.append(x)
        elif(self.min[len(self.min)-1]>x):
            self.min.append(x)
        self.stack.append(x)

    def pop(self):
        
        if(len(self.stack)==0):
            return 
        if(self.stack.pop()==self.min[len(self.min)-1]):
            self.min.pop()

    def top(self):
        if(len(self.stack)==0):
            return None
        return self.stack[len(self.stack)-1]

    def getMin(self):
        return self.min.pop()

s1 = MinStack()
s1.push(1)
s1.push(9)
s1.push(1)
s1.push(2)
print(s1.stack)
s1.pop()
print(s1.stack)
print(s1.top())
print('min:',s1.getMin())
s2= MinStack()
s2.pop()
print(s2.top())
