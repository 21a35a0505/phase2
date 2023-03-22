import random
b=int(input("how many points :"))
sd=0
pd=0
print("1=rock")
print("2=paper")
print("3=scissors")
print()
while(sd<=b):
    c=random.randint(1,3)
    d=int(input("user choice : "))
    print("computer choice :",c)
    print()
    if(d>=4):
        print("invalid number")
        print()
    if (c==2 and d==1) or (c==3 and d==2) or (c==1 and d==3) :
        pd=pd+1
        print("computer score :",pd,end="  ")
        print("user score :",sd)
        print()
    elif (c==1 and d==2) or (c==2 and d==3) or (c==3 and d==1):
        sd=sd+1
        print("user score :",sd,end="  ")
        print("computer score :",pd)
        print()
    if(d==c):
        print("draw")
    if(sd==b):
        break
    else:
        if(pd==b):
            break
if(sd==b):
    print()
    print("user is winner")
else:
    print()
    print("computer is winner")

