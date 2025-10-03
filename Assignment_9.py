class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def enqueue(self,item):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            item = self.queue.pop(0)
            return item
        
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.queue[0]
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.size
        
    def display(self):
        print("Queue: ",self.queue)

q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.display()
print("Top element is:", q.peek())
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()