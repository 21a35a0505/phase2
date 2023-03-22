temp=[]
ori=[1,2,3,4,5,6]
pos=0
key=int(input())
found=False
for i in range(len(ori)):
    val=(ori.pop())
    temp.append(val)
    if val==key:
        pos=i
        found=True
if found:
    print("element found at position:",pos)
else:
    print("Not found")
