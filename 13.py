#13. Find Duplicates in an Array
def fd(arr):
     n=len(arr)
     s=sum(arr)
     u= sum(set(arr))
     d=s-u
     print(d)

fd(arr=[1,2,3,4,5,5,6,7,8])