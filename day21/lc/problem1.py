# 2657. Find the Prefix Common Array of Two Arrays

def findThePrefixCommonArray(A,B):
    n=len(A)
    c=[0]
    if A[0]==B[0]:
        c=[1]
    for i in range(1,n):

        temp=c[i-1]
        if A[i]==B[i]:
            temp+=1
        else:
            for j in range(i):
                if A[j]==B[i] :
                    temp+=1
                
                if  B[j]==A[i] :
                    temp+=1
            
        
        c.append(temp)
    return c

A = [1,2,3,4,5,6,7,8,9,0]
B = [0,9,8,7,6,5,4,3,2,1]
print(findThePrefixCommonArray(A,B))