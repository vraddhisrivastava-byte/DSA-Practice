# Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.
def pair(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                print(arr[i], arr[j])

pair([1, 2, 3, 4, 5], 5)