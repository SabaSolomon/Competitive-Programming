from collections import deque

stack = []

queue = deque()

def enqueue(stack, num):
    stack.append(num)
    
def dequeue(stack):
    if(len(stack) > 0):
        return stack.pop(0)
    return None

def push(queue, num):
    queue.append(num)

  
def pop(queue):
    return queue.popleft()
    


# Stack with queue
push(queue, 8);
push(queue, 4);
push(queue, 3);

print("Stack: ", queue)
print("pop: ",pop(queue))
push(queue, 9)
print("Stack: ", queue)

# Queue with stack
enqueue(stack, 2)
enqueue(stack, 4)
enqueue(stack, 1)

print("Queue: ", stack)
print("Dequeue: ",dequeue(stack))
print("Queue: ", stack)
