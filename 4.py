#4. Find the Second Largest Element.
def secondlarge(arr):
    arr = list(set(arr))
    if len(arr) < 2:
        return None
    print (arr[-2])
secondlarge([2,4,2,1,5,6,8,7,9,4,0,10,6,7,8])