def merge(left_half,right_half):
    s=[]
    while len(left_half)!=0 and len(right_half)!=0:
        if left_half[0]<right_half[0]:
            s.append(left_half.pop(0))
        else:
            s.append(right_half.pop(0))
    if len(left_half)>0:
        s=s+left_half
    elif len(right_half)>0:
        s=s+right_half
    return s
def merge_sort(l):
    if len(l)<=1:
        return l
    else:
        left_list=l[:len(l)//2:]
        right_list=l[len(l)//2:]
        left_list=merge_sort(left_list)
        right_list=merge_sort(right_list)
        return merge(left_list,right_list)
a=list(map(int,input().split()))
print(merge_sort(a))
    
        
    
    
