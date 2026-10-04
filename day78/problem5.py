# 835. Image Overlap



def largestOverlap(img1,img2):
    n=len(img1)
    ans=0
    for i in range(-(n-1),n):
        for j in range(-(n-1),n):
            forward=0
            for x in range(n):
                for y in range(n):
                    if  0<=x+i<n and 0<=y+j<n:
                        if img1[x][y]==1 and img2[x+i][y+j]==1:
                            forward+=1
            ans=max(ans,forward)
    return ans