class stack:
    def __init__(self):
        self.stack = []
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        if self.is_empty():
            return "Stack is Underflow!"
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
    def peek(self):
        if self.is_empty():
            return "Stack is Empty!"
        return self.stack[-1]
    def display(self):
        return self.stack
st= stack()
st.push(39)
st.push(6)
st.push(74)
st.push(12)
print(st.display())
st.pop()
print(st.display())