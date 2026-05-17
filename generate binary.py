"""from collections import deque
def generate_binary(n):
    q=deque(['1'])
    res=[]
    for _ in range(n):
        print(_)

generate_binary(5) """

from collections import deque
def generate_binary(n):
    q=['1']
    res=[]
    for i in range(n):
        curr=q.pop(0)
        res.append(curr)
        q.append(curr+'0')
        q.append(curr+'1')
    return res
print(generate_binary(5))