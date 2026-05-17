 #20.Rotate Array by k Positions: Rotate the array to the left by k positions.
def rotate(arr,k):
    n=len(arr)
    k=k%n
    arr[:]= arr[-k:]+arr[:-k]
    print(arr)
rotate(arr=[1,2,3,4,5,6],k=4)