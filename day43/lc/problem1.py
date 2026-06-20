# 3552. Grid Teleportation Traversal

from collections import deque,defaultdict
def minMoves(matrix):
    n=len(matrix)
    m=len(matrix[0])
    portal=defaultdict(list)
    for i in range(n):
        for j in range(m):
            if 65<=ord(matrix[i][j])<=90:
                portal[matrix[i][j]].append((i,j))
    q=deque()
    portalvis=set()
    seen=set()
    seen.add((0,0))
    if matrix[0][0] != ".":
        for i,j in portal[matrix[0][0]]:
            q.append((i,j))
            seen.add((i,j))
        portalvis.add(matrix[0][0])
    else:
        q.append((0,0))
    direction=[(1,0),(0,1),(-1,0),(0,-1)]
    moves=0
    while q:
        l=len(q)
        for _ in range(l):
            r,c=q.popleft()
            if r==n-1 and c==m-1:
                return moves
            for x,y in direction:
                nr=r+x
                nc=c+y
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in seen :
                    if matrix[nr][nc]=="#":
                        continue
                    elif matrix[nr][nc] != "." and matrix[nr][nc] not in portalvis:
                        portalvis.add(matrix[nr][nc])
                        for i,j in portal[matrix[nr][nc]] :
                            q.appendleft((i,j))
                            seen.add((i,j))
                    else:
                        q.append((nr,nc))
                    seen.add((nr,nc))
        moves+=1
    return -1

mat=[".#...",".#.#.",".#.#.","...#."]
print(minMoves(mat))