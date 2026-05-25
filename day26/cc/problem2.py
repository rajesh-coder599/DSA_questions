# Magical Planks


t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if n==1:
        print(0)
        continue
    w=0
    b=0
    if s[0]=="W":
        w+=1
    else:
        b+=1
    for i in range(1,n):
        if s[i]!=s[i-1]:
            if s[i]=="W" :
                w+=1
            else:
                b+=1
    print(min(w,b))