#  2229A. Slimes on a Line



t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    a=min(arr)
    b=max(arr)
    c=b-a
    ans=c//2+c%2
    print(ans)