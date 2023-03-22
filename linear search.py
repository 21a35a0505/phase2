a=[1,2,3,4,5,6,7,8,9]
key=int(input())
found=False
for i in range(len(a)):
    if key==a[i]:
        print('key is found at position',i+1)
        found=True
        break
if not found:
    print("Element Not Found")
