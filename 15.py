#15. Find Union of Two Arrays
def union(arr1,arr2):
    arr1.extend(arr2)
    uarr1=list(set(arr1))
    print(uarr1)
union([1,2,3,4],[3,4,5,6])

