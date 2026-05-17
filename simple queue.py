class linearqueue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[None]*capacity
        self.front=self.rear=-1
    def is_full(self):
        return self.rear==self.capacity-1
    def is_empty(self):
        return self.front==-1
    def enqueue(self,element):
        if self.is_full():
            print("queue is overflow")
            return
            if self.front==-1:
                self.front+=1
            self.rear+=1
            self.queue[self.rear]=element
            print(f"insert an element:{element}")
    def dequeue(self):
        if self.is_empty():
            print("queue is underflow")
            return
        element=self.queue[self.front]
        self.queue[self.front]=None
        if self.front==self.rear:
            print("we removed last element")
            self.front=self.rear=-1
        else:
            self.front+=1
        return element
    def peek(self):
        if self.is_empty():
            print("queue is empty")
            return
        return self.queue[self.front]
    def display(self):
        if self.is_empty():
            print("queue is empty")
        else:
            print(f"queue:{self.queue}")

q=linearqueue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.display())