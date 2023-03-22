def Quick_sort(arr):
    if len(arr)<1:
        return arr
    pivot=arr[0]
    left=[i for i in arr[1:] if i<pivot]
    right=[i for i in arr[1:] if i>pivot]
    return Quick_sort(left)+pivot+Quick_sort(right)
arr=list(map(int,input().split()))
arr=Quick_sort(arr)
print(arr)
    
