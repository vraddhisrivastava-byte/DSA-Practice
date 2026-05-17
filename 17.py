#17. Find the Leader Elements: An element is a leader if it is greater than all elements to its right.
def leader(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]<=arr[j]:
                break   
        if j == n-1: 
            print(arr[i], end=" ") 
leader(arr=[16,17,4,3,5,2])