class staticstack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack=[None]*capacity
        self.top=-1
    def push(self,ele):
        if self.top==self.capacity-1:
            print ("Stack is Overflow! we cannot perform push operation")
            return
        self.top+=1
        self.stack[self.top]=ele
        print(f"ADDED{ele} in stack")
    def pop(self):
        if self.top==-1:
            print ("Stack is Underflow! we cannot perform pop operation")
            return
        ele=self.stack[self.top]
        self.top-=1
        return ele
    def peek(self):
        if self.top==-1:
            print ("Stack is Empty!")
        return self.stack[self.top]
    def is_full(self):
        return self.top==self.capacity-1
    def display(self):
        return self.stack

stack = staticstack(6)
print(type(stack))
print(stack.display())
stack.push("Hello")
stack.push("Namaste")
stack.pop()
stack.push("Hi")
print(stack.display())