class simpliqueue:
    def __init__(self,size):
        self.queue=[]
        self.size=size
    def enqueue(self,element):
        if len (self.queue)<self.size:
            self.queue.append(element)
            print(f"element enqueued:{element}")
        else:
            print("queue is overflow")
    def dequeue(self):
        if not self.queue:
            return ("queue is underflow")
        return self.queue.pop(0)
    def display(self):
        return self.queue
    
q=simpliqueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.display())