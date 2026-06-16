# CAO Stage-1



t=int(input())
for _ in range(t):
    r,c=map(int,input().split())
    grid=[list(input().strip()) for _ in range(r)]
    left=[[0 for _ in range(c)] for _ in range(r)]
    right=[[0 for _ in range(c)] for _ in range(r)]
    up=[[0 for _ in range(c)] for _ in range(r)]
    down=[[0 for _ in range(c)] for _ in range(r)]

    ## left
    for i in range(r):
        for j in range(c):
            if grid[i][j]=="^":
                left[i][j]=1+(left[i][j-1] if j>0 else 0)
    
    ## right
    for i in range(r):
        for j in range(c-1,-1,-1):
            if grid[i][j]=="^":
                right[i][j]=1+(right[i][j+1] if j<c-1 else 0)

    ## up
    for i in range(r):
        for j in range(c):
            if grid[i][j]=="^":
                up[i][j]=1+(up[i-1][j] if i>0 else 0)
    
    ## down
    for i in range(r-1,-1,-1):
        for j in range(c):
            if grid[i][j]=="^":
                down[i][j]=1+(down[i+1][j] if i<r-1 else 0)
    
    ans=0
    for i in range(r):
        for j in range(c):
            l=left[i][j]-1
            r=right[i][j]-1
            u=up[i][j]-1
            d=down[i][j]-1
            if min(l,r,u,d)>=2:
                ans+=1
    print(ans)