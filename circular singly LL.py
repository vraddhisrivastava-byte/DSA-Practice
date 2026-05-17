class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularSinglyLL:
    def __init__(self):
        self.head = None
    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
    def insert_after_node(self, target, data):
        if not self.head:
            print("list is empty")
            return
        temp = self.head
        while True:
            if temp.data==target:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print("target not found")
    def display(self):
        if not self.head:
            print("list is empty")
            return
        temp = self.head
        while True:
            print(f"{temp.data}", end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("HEAD")
    def delete_start(self):
        if not self.head:
            print("list is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
    def delete_end(self):
        if not self.head:
            print("list is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            curr = self.head
            while curr.next != self.head:
                prev = curr
                curr = curr.next
            prev.next = self.head
    def delete_value(self, key):
        if not self.head:
            print("list is empty")
            return
        curr = self.head
        prev= None
        if curr.data == key:
            self.delete_start()
            return
        while True:
            prev = curr
            curr = curr.next
            if curr == self.head:
                print("key not found")
                break
            if curr.data == key:
                prev.next = curr.next
                return
CLL = CircularSinglyLL()
CLL.insert_at_start(10)
CLL.insert_at_end(20)
CLL.insert_after_node(10, 15)
CLL.delete_end()
CLL.display()
CLL.delete_start()
CLL.insert_at_start(5)
CLL.insert_at_end(25)
CLL.insert_after_node(15, 17)
CLL.display()