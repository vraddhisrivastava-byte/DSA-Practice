from collections import deque
def is_pali_queue(word):
    q=deque(word)
    while len(q)>1:
        if q.popleft()!=q.pop():
            return False
    return True
st="naman"
if is_pali_queue(st):
    print("queue is palindrome")
else:
    print("queue is not palindrome")