# https://codeforces.com/contest/2252/problem/C
# C. Risky Tower


## WA (wrong approach)
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    stablity=list(map(int,input().split()))
    jenga=[list(map(int,input().split())) for _ in range(n)]
    min_stablity=float("inf")
    ans=float("inf")
    for i in range(n):
        arr=jenga[i]
        arr.sort(reverse=True)
        min_stablity=min(min_stablity,stablity[i])
        curr_destablization=0
        moves=0
        for j in arr:
            curr_destablization+=j
            moves+=1
            if curr_destablization>=min_stablity:
                break
        ans=min(moves,ans)
    print(ans)