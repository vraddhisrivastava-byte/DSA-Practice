#3. Find the Sum of Elements
def sum(arr):
    a=0
    for i in range(len(arr)):
        a=a+arr[i]
    print ("sum of array:",a)

sum([1,2,3,4])