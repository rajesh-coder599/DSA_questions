# 1861. rotating the box

grid=[["#",".",".",".","."],["#","*","#","*","."],["#","#","#","#","#"],["#","#","#","#","#"]]
def rotatethebox(grid):
    row=len(grid)
    col=len(grid[0])

    for i in range(row):
        l=None
        r=None
        for j in range(col):
            if l==None and r==None :
                if grid[i][j]=="#":
                    l=j
                    r=j
            elif l!=None and r !=None :
                if grid[i][j]=="#":
                    r+=1
                elif grid[i][j]==".":
                    grid[i][l]="."
                    l+=1
                    r+=1
                    grid[i][r]="#"
                else:
                    l=None
                    r=None
    grid.reverse()
    rotated_grid=[[-1 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            rotated_grid[j][i]=grid[i][j]
    return rotated_grid

print(rotatethebox(grid))