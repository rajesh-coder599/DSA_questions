# 4016. Maximum Area of Two Non-Overlapping Square Submatrices



## need some didd touch
def maxArea(mat):
    from collections import deque
    n=len(mat)
    m=len(mat[0])
    vis=set()
    def bfs(i,j):
        k=0
        q=deque([(i,j)])
        vis.add((i,j))
        while q:
            k+=1
            l=len(q)
            check=True
            for _ in range(l):
                r,c=q.popleft()
                temp=[]
                for x,y in [(1,0),(0,1),(1,1)]:
                    nr=r+x
                    nc=c+y
                    if nr>=n or nc>=m  or (nr,nc) in vis or (nr<n and nc<m and mat[nr][nc]!=1):
                        check=False
                        break
                    temp.append((nr,nc))
                if check:
                    for i in temp:
                        q.append(i)
                        vis.add(i)
                if not check:
                    break
            if not check:
                break
        return k
    possible=[]
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1 and (i,j) not in vis:
                temp=bfs(i,j)
                print((i,j),temp)
                possible.append(temp)
    possible.sort(reverse=True)
    if len(possible)==0:
        return 0
    for i in range(len(possible)-1):
        if possible[i]==possible[i+1]:
            return possible[i]
    return possible[0]//2

grid=[[0,1,1,1,1,1,1,0],[1,1,1,1,0,1,0,1],[1,1,0,0,1,1,1,1]]
print(maxArea(grid))
print(2//2)