# 909. Snakes and Ladders


from collections import deque
def snakesAndLadders(board):
    n=len(board)
    currnum=1
    getposition={}
    check=0
    for i in range(n-1,-1,-1):
        if check%2==0:
            for j in range(n):
                getposition[currnum]=(i,j)
                currnum+=1
        else:
            for j in range(n-1,-1,-1):
                getposition[currnum]=(i,j)
                currnum+=1
        check+=1
    q=deque([(1,0)])
    vis={1}
    while q:
        node,move=q.popleft()
        for nxt in range(node+1,min(node+6,n**2)+1):
            r,c=getposition[nxt]
            if board[r][c] != -1:
                nxt=board[r][c]
            if nxt==n**2:
                return move+1
            if nxt not in vis:
                vis.add(nxt)
                q.append((nxt,move+1))
    return -1
