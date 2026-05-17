def max_dishes(arr,n):
    count=[]
    for i in range(1,n):
        for j in range (i,n):
            if arr[i]==arr[j]:
                count.append(i)
    return count

print(max_dishes([1,1,1,2,1,2,1,1,2],9))

