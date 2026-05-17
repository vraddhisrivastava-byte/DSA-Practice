#2. Find the Maximum & Minimum Element
def maxnmin(arr):
    max=arr[0]
    min=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]

    print("max number",max)
    print("min number",min)
maxnmin([1,3,5,7,8,9,4])