class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
    def insert_at_end(self, data):
        new_node= Node(data)
        if not self.head:
            self.head = new_node
            return
        temp= self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def insert_inbetweeen(self, target, data):
        new_node= Node(data)
        temp= self.head
        while temp and temp.data != target:
            temp = temp.next
        if temp:
            new_node= Node(data)
            new_node.next= temp.next
            temp.next = new_node
        else:
            print("target not found")
    def display(self):
        if not self.head:
            print("list is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
LL= LinkedList()
LL.insert_at_start(10)
LL.insert_at_end(20)
LL.insert_inbetweeen(10, 15)
LL.display()
