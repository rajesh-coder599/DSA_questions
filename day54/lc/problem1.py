# 1260. Shift 2D Grid


def shiftGrid(grid,k):
    row=len(grid)
    col=len(grid[0])
    k%=row*col
    if k==0 :
        return grid
    prev=grid[row-1][col-1]
    for _ in range(k):
        for i in range(row):
            for j in range(col):
                temp=prev
                prev=grid[i][j]
                grid[i][j]=temp
    return grid