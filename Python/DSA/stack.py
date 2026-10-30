MAX = 5

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.is_full():
            print("Stack overflow")
            return
        self.stack.append(x)
    
    def pop(self):
        self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    
    def is_full(self):
        return len(self.stack) == MAX

    def display(self):
        for i in self.stack:
            print(i)

    def top(self):
        print(self.stack[-1])


class Queue:
    def __init__ (self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return self.rear == MAX - 1
    

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        
        return "queue is empty "

    def display (self):
        print("Queue state :", self.queue)

    def top(self):
            print(self.queue[-1])

s = Stack()

q = Queue()

num1 = int(input())
s.push(num1)


num2 = int(input())
q.enqueue(num2)

