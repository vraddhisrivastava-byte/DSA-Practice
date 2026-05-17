#24. Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.
def rearrange(arr):
    max=arr[0]
    min=arr[0]
    a=[]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
    a.append(max,min)
    