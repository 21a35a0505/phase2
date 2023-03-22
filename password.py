n=int(input())
for i in range(n):
    paswrd=input()
    if len(paswrd)>=8 and len(paswrd)<16:
        if paswrd[i].isalpha:
            uc=False
            lc=False
            num=False
            spl=False
            lower="qwertyuiopasdfghjklzxcvbnm"
            upper="QWERTYUIOPASDFGHJKLZXCVBNM"
            for i in paswrd:
                if i.isdigit():
                    num=True
                elif i in upper:
                    uc=True
                elif i in lower:
                    lc=True
                else:
                    spl=True
            if(uc and lc and num and spl):
                print("true")
            else:
                print("False")
        else:
            print("False")
    else:
        print("False")
