# A. Destroying Towers


t=int(input())
for _ in range(t):
    n=int(input())
    height=list(map(int,input().split()))
    minsum=0
    currmnheight=float("inf")
    for i in height:
        currmnheight=min(currmnheight,i)
        minsum+=currmnheight
    print(minsum)