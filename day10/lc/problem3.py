# 48. rotate image (in place)


matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
def rotate(matrix):
    n=len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    return matrix

print(rotate(matrix))


# k times

k=3
def rotate(matrix,k):
    n=len(matrix)
    
    for _ in range(k%4):
        matrix.reverse()
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    return matrix

print(rotate(matrix,k))