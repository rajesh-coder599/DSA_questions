# 01 matrix

mat=[[0,0,0],[0,1,0],[0,0,0]]
m=len(mat)
n=len(mat[0])
ans=[[0]*m]*n
def nearestzero(i,j,mat,ans):
    
    if i==n-1 and j==m-1:
        return mat[i][j]

    right=mat[i][j]+nearestzero(i,j+1,mat,ans)
    left=mat[i][j]+nearestzero(i,j-1,mat,ans)
    down=mat[i][j]+nearestzero(i+1,j,mat,ans)
    up=mat[i][j]+nearestzero(i-1,j,mat,ans)
    ans[i][j]=min(right,left,down,up)

    return ans
        
print(nearestzero(0,0,mat,ans))
print(ans)
