a=list(map(int,input().split(',')))
a.sort()
key=int(input())
low=0
high=len(a)-1
mid=(low+high)//2
found=False
l=[]
while low<high:
    if a[mid]==key:
        found=True
        while a[mid-1]==key:
            mid=mid-1
            if mid==0:
                break
        while a[mid]==key:
            l.append(mid)
            mid=mid+1
            if mid==len(a):
                mid=mid-1
                break 
        print(l)
    elif a[mid]<key:
        low=mid+1
    elif a[mid]>key:
        high=mid-1
if found==False:
    print(-1)
