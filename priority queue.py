class PriorityQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self,value,priority):
        data=[priority,value]
        if not self.queue:
            self.queue.append(data)
        else:
            add=False
            for i in range(len(self.queue)):
                if priority < self.queue[i][0]:
                    self.queue.insert(i,data)
                    add=True
                    break
            if not add:
                self.queue.append(data)
    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop()
    def display(self):
        print(self.queue)

pq=PriorityQueue()
pq.enqueue(3)
pq.enqueue(1)
pq.enqueue(2)
pq.display()

