#6. Check if Array is Sorted
def sortarray(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
print(sortarray([5,0,4,6]))












