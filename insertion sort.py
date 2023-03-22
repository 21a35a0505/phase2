def Insertion_sort(a):
    for i in range(1,len(a)):
        j=i
        while a[j-1]>a[j] and j>0:
            a[j],a[i]=a[i],a[j]
            j-=1
    print(a)

Insertion_sort([3,6,1,9,7,4,8])
            
