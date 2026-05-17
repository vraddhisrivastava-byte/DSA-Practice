class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(self.root, data)
    def insert_node(self, current_node, data):
        if data< current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self.insert_node(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self.insert_node(current_node.right, data)
    def display(self):
        if not self.root:
            print("The tree is empty.")
            return
        self.display_tree(self.root,"",True)

    def display_tree(self, node, space, last):
        if node is not None:
            print(space, end="")
            if last:
                print("R>", end="")
                space+="    "
            else:
                print("L>", end="")
                space+="     "
            print(node.data)
            self.display_tree(node.left, space, False)
            self.display_tree(node.right, space, True)
    def search(self,key):
        return self.search_key(self.root,key)
    def search_key(self, curr,key):
        if curr is None or curr.data == key:
            return curr
        if key<curr.data:
            return self.search_key(curr.left,key)
        return self.search_key(curr.right,key)






nums=[50,30,20,40,70,60]

bst= BinarySearchTree()
for i in nums:
    bst.insert(i)
bst.display()
key= 67
res= (bst.search)
if res:
    print(f"Key {key} found in the BST.")
else:
    print(f"Key {key} not found in the BST.")