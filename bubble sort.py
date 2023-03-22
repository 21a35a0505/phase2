
def Bubble_sort(a):
    for i in range(len(a)):
        swap=False
        for j in range (i+1,len(a)):
            if a[j]<a[i]:
                a[j],a[i]=a[i],a[j]
                swap=True
        if swap==False:
            break
a=[2,6,8,1,4,9,3]
Bubble_sort(a)
print(a)
'''
a=[[1,2],[3,4],[2,1],[16,3]]
for i in range(4-1):
    for j in range(4-i-1):
        if a[j][0]<a[j+1][1]:
            a[j][1],a[j+1][1]=a[j+1][1],a[j][1]
print(a)
    
'''
