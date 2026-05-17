#11. Remove given Element from Array
def removearr(arr,e):
    if e not in arr:
        print("element not in array",arr)
    else:
        arr.remove(e)
        return arr
print(removearr([1,2,3,4,5,6,7,8,9],5))