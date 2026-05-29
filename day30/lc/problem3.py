# 130. Surrounded Regions



def solve(board):
    rows=len(board)
    col=len(board[0])
    visited=set()
    def dfs(i,j):
        if i<0 or j<0 or i>=rows or j>=col:
            return
        if board[i][j]=="X":
            return
        if (i,j) in visited:
            return
        visited.add((i,j))
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
    for i in range(col):
        if board[0][i]=="O" and (0,i) not in visited:
            dfs(0,i)
    for i in range(col):
        if board[rows-1][i]=="O" and (rows-1,i) not in visited:
            dfs(rows-1,i)
    for j in range(rows):
        if board[j][0]=="O" and (j,0) not in visited:
            dfs(j,0)
    for j in range(rows):
        if board[j][col-1]=="O" and (j,col-1) not in visited:
            dfs(j,col-1)
    def change(r,c):
        if r<0 or c<0 or r>=rows or c>=col:
            return
        if board[r][c]=="X":
            return
        if (r,c) in visited:
            return
        board[r][c]="X"
        visited.add((r,c))
        change(r+1,j)
        change(r-1,j)
        change(r,c+1)
        change(r,c-1)
    for x in range(rows):
        for y in range(col):
            if board[x][y]=="O" and (x,y) not in visited:
                change(x,y)
    return board