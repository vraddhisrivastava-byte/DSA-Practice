#10. Merge Two Sorted Arrays
def mergearray(arr,brr):
    arr.extend(brr)
    arr=list(set(arr))
    print (arr)
   
mergearray([1,2,3,4],[5,6,7,8])