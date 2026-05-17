
#9. Remove Duplicates from Array: Remove duplicates from the array while maintaining order.
def duplicate(arr):
    f={}
    n={}
    for i in arr:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
            if f[i]>0:
                n[i]=f[i]
    print(f)
    print (n)
    print (list(n.keys()))
   
duplicate([8,1,2,1,3,4,5,4,2,7,3,8,4,7,8,0,0])