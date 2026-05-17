#14. Find Intersection of Two Arrays: Find the common elements between two arrays.
def intersection(arr1, arr2):
    I=[]
    for i in arr1:
        for j in arr2:
            if i==j:
                I.append(i)
    print(I)
intersection([1,2,3,4,5],[4,5,6,7,8])