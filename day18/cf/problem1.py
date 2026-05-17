# 2093B. Expensive Number


t=int(input())
for _ in range(t):
    n=input()
    zeros=n.count("0")
    right_zeros=0
    for i in range(len(n)-1,-1,-1):
        if n[i]=="0":
            right_zeros+=1
        else:
            break
    zeros-=right_zeros
    a=len(n)-zeros-1
    print(a)