# 62. Unique paths

m=3
n=7
def uniquepath(i,j,n,m,dp):
    if i==n-1 and j==m-1:
        return 1
    if i>=n or j>=m:
        return 0
    if dp[i][j] != -1 :
        return dp[i][j]
    right=uniquepath(i+1,j,n,m,dp)
    down=uniquepath(i,j+1,n,m,dp)
    dp[i][j]=right+down
    return dp[i][j]

dp=[[-1 for _ in range(m)] for _ in range(n)]
print(uniquepath(0,0,n,m,dp))

# by formula
# t=O(1)
# s=O(1)
a=m+n-2
print(int(((a-1)*a)/2))