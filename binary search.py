a=list(map(int,input().split()))
a.sort()
key=int(input())
low=0
high=len(a)-1
while(low<=high):
    mid=(low+high)//2
    if (a[mid]==key):
        print("element found at position",mid)
        break
    elif a[mid]>key:
        high=mid-1
    elif a[mid]<key:
        low=mid+1
    else:
        print("Element not found")
