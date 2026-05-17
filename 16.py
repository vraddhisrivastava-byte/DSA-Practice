#16. Check if Two Arrays Are Equal: if two arrays contain the same elements
def check(arr1,arr2):
    if sorted(arr1)==sorted(arr2):
        print("Equal")
    else:
        print("Not Equal")

check([1,1,2,3,4],[1,2,3,4])