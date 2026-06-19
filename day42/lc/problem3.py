# 529. Minesweeper


def updateBoard(board,click):
    from collections import deque
    n=len(board)
    m=len(board[0])
    seen=set()
    seen.add((click[0],click[1]))
    q=deque([(click[0],click[1])])
    if board[click[0]][click[1]]=="M":
        board[click[0]][click[1]]="X"
        return board
    directions=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)]
    while q:
        l=len(q)
        for _ in range(l):
            r,c=q.popleft()
            minecount=0
            for x,y in directions:
                nr=r+x
                nc=c+y
                if 0<=nr<n and 0<=nc<m:
                    if board[nr][nc]=="M":
                        minecount+=1
            if minecount==0:
                board[r][c]="B"
                for x,y in directions:
                    nr=r+x
                    nc=c+y
                    if 0<=nr<n and 0<=nc<m:
                        if (nr,nc) not in seen:
                            seen.add((nr,nc))
                            q.append((nr,nc))
            else:
                board[r][c]=str(minecount)
    return board