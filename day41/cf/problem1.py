# A. Game with a Fraction


t=int(input())
for _ in range(t):
    p,q=map(int,input().split())
    k=abs(p-q)
    if abs(k*2-p)==abs(k*3-q) and k*2<=p and k*3<=q and p!=q:
        print("Bob")
    else:
        print("Alice")