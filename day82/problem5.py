# 1267. Count Servers that Communicate



def countServers(grid):
    n=len(grid)
    m=len(grid[0])
    count=[0]*(n+m)
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                count[i]+=1
                count[n+j]+=1
    ans=0
    for i in range(n):
        for j in range(m):
            if (count[i]>1 or count[n+j]>1) and grid[i][j]:
                ans+=1
    print(count)
    return ans

mat = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
print(countServers(mat))