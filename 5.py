#5. Count Frequency of Elements
def cf(arr):
    f = {}
    
    for i in arr:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    print(f)
cf([2,3,4,2,3,4,5,6,3,2,2,4,6])