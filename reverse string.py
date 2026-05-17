from collections import deque
def reverse_string(s):
    q=deque()
    for char in s:
        q.append(char)
    res=""
    while q:
        res+=q.pop()
    return res
st="abc"
print(reverse_string(st))