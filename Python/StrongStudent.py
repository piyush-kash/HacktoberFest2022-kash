def diffSum(n, m, arr): 
    # code here 
    arr.sort()
    return (sum(arr[len(arr)-m:])-sum(arr[:m]))

# N = 5, M = 4
# A = {1 2 3 4 5}