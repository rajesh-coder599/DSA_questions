# https://codeforces.com/problemset/problem/2240/B
# B. AI Finds Nothing Here


t=int(input())
for _ in range(t):
    n,m,r,c=map(int,input().split())
    submat=(n-r+1)*(m-c+1)
    mat=n*m
    mod=998244353
    exp=mat-submat
    print(pow(2,exp,mod))