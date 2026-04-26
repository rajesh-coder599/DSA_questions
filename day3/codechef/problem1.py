# TCS Examination
t=int(input())
for i in range(t):
    d=list(map(int,input().split()))
    s=list(map(int,input().split()))
    dt=sum(d)
    st=sum(s)
    if dt>st:
        print("Dragon")
    elif st>dt:
        print("Sloth")
    else:
        if d[0]>s[0]:
            print("Dragon")
        elif d[0]<s[0]:
            print("Sloth")
        else:
            if d[1]>s[1]:
                print("Dragon")
            elif d[1]<s[1]:
                print("Sloth")
            else:
                print("Tie")