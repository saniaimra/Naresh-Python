class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self,item):
        if self.is_full():
            print("Stack is full")
        else:
            self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            item = self.stack.pop()
            return item
        
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.size
        
    def display(self):
        print("Stack: ",self.stack)
s = Stack(5)   

s.push(10)
s.push(20)    
s.push(30)
s.push(40)
s.push(50)

s.display()

print("Top element is:", s.peek())

s.pop()
s.display()
s.pop()
s.display()
s.pop()
s.display()
s.pop()
s.display()
s.pop()
s.display()
s.pop()
    

    