# https://codeforces.com/problemset/problem/136/A
# A. Presents



n=int(input())
arr=list(map(int,input().split()))
ans=[-1]*n
for i in range(n):
    ans[arr[i]-1]=i+1
print(*ans)