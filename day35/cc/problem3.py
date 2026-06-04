# Interesting XOR!


t=int(input())
for _ in range(t):
    c=int(input())
    a=1
    while a<=c:
        a*=2
    b=c^(a-1)
    bit=""
    d=c
    while d>1:
        temp=d%2
        bit=str(temp)+bit
        d//=2
    bit="1"+bit
    x=b
    y=b
    check=False
    n=len(bit)
    for i in range(n):
        if bit[i]=="1":
            if not check:
                x+=(2**(n-i-1))
                check=True
            else:
                y+=(2**(n-i-1))
    print(x*y)