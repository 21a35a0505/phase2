a='axaxdxaxr'
l=[' ']
for i in range(len(a)):
    s=a[i]
    for j in range(i+1,len(a)):
        if a[i]!=a[j]:
            if len(s)>=2:
                if len(l[0])>=len(s):
                    pass
                else:
                    l.pop(0)
                    l.append(s)
            break
        else:
            s=s+a[j]
print(l[0]) 
