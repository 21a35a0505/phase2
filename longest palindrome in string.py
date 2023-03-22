s=input()
pal=[]
le=[]
for i in range(len(s)):
    for j in range(-1,-len(s)-1,-1):
        s1=s[i:len(s)+j+1]
        s2=s[j:-len(s)-1+i:-1]
        print(s1,s2)
        if s1==s2:
            if i!=len(s)+j:
                pal.append(s1)
for i in pal:
    le.append(len(i))
p=le.index(max(le))
print(pal[p])

s=input()
pal=[]
le=[]
for i in range(len(s)):
    for j in range(-1,-len(s)-1,-1):
        s1=s[i:len(s)+j+1]
        s2=s[j:-len(s)-1+i:-1]
        print(s1,s2)
        if s1==s2:
            if i!=len(s)+j:
                pal.append(s1)
for i in pal:
    le.append(len(i))
p=le.index(max(le))
print(pal[p])