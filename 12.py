#12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.
def missing(arr):
    n=len(arr)
    i=n*(n+1)//2
    u= sum(set(arr))
    m=i-u

    return(m)
print(missing([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]))