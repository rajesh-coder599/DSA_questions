# 4052. Cyclically Shift Rows and Columns




def cyclicShift(n,grid,rowShift,colShift):
    for i in range(n):
        for _ in range(rowShift[i]):
            for k in range(n-1):
                grid[i][k],grid[i][k+1]=grid[i][k+1],grid[i][k]
    for i in range(n):
        for _ in range(colShift[i]):
            for k in range(n-1):
                grid[k][i],grid[k+1][i]=grid[k+1][i],grid[k][i]
    return grid