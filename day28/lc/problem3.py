# 79. Word Search

def exist(board,word):
    rows=len(board)
    col=len(board[0])

    def dfs(r,c,n):
        if n==len(word):
            return True
        
        if r<0 or c<0 or r>=rows or c>=col or board[r][c]!=word[n]:
            return False
        
        temp=board[r][c]
        board[r][c]="#"

        found=(dfs(r+1,c,n+1) or dfs(r-1,c,n+1) or dfs(r,c+1,n+1) or dfs(r,c-1,n+1))

        board[r][c]=temp

        return found
    
    for i in range(rows):
        for j in range(col):

            if dfs(i,j,0) :
                return True
        
    return False

b=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
w="ABCCED"
print(exist(b,w))