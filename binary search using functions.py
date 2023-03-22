def binarysearch(arr,low,high,key):
    mid=(low+high)//2
    found=False
    if arr[mid]==key:
        found=True
        print('element found at index',mid)
        
    elif arr[mid]<key:
        low=mid+1
        return binarysearch(arr,low,high,key)
    elif arr[mid]>key:
        high=mid-1
        return binarysearch(arr,low,high,key)
    elif (mid==low and arr[mid]!=key)or (mid==high and arr[mid]!=key):
        print('ele not found')

arr=list(map(int,input().split()))
key=int(input())
arr.sort()
binarysearch(arr,0,len(arr),key)

'''
reverse 1st half of a stack
reverse last half of queue'''
