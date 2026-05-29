# 419. Battleships in a Board


def countBattleships(board):
    rows=len(board)
    col=len(board[0])
    visited=set()
    battelship=0
    def dfs(i,j):
        if i<0 or j<0 or i>=rows or j>=col :
            return
        if board[i][j]==".":
            return
        if (i,j) in visited:
            return
        visited.add((i,j))
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
    for r in range(rows):
        for c in range(col):
            if board[r][c]=="X" and (r,c) not in visited:
                battelship+=1
                dfs(r,c)
    return battelship