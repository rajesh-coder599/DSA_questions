# 733. Flood Fill


def floodFill(image,sr,sc,color):
    rows=len(image)
    col=len(image[0])
    x=image[sr][sc]
    def dfs(i,j):
        if i<0 or j<0 or i>=rows or j>=col :
            return
        if image[i][j]!=x:
            return
        image[i][j]=color
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
    if x==color:
        return image
    dfs(sr,sc)
    return image
mt=image = [[1,1,1],[1,1,0],[1,0,1]]
i=1
j=1
c=2
print(floodFill(mt,i,j,c))