class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head= None
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def insert_after(self, target, data):
        temp= self.head 
        while temp and temp.data != target:
            temp = temp.next
        if temp:
            new_node = Node(data)
            new_node.next = temp.next
            new_node.prev = temp
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node
        else:
            print(f"target {target} not found")
    def delete_node(self, key):
        temp = self.head
        if not temp:
            print("LL is empty")
            return
        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
        while temp and temp.data != key:
            temp = temp.next
        if not temp:
            print(f"key {key} not found")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
    def display(self):
        temp= self.head
        while temp:
            print(f"{temp.data}<->", end=" ")
            temp = temp.next
        print("None")

dll= DoublyLinkedList()
dll.insert_at_start(10)
dll.insert_at_end(20)
dll.insert_at_start(5)
dll.insert_at_end(25)
dll.insert_after(10, 15)
dll.delete_node(20)
dll.delete_node(5)
dll.display()
