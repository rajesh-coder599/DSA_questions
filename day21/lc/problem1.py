# 2657. Find the Prefix Common Array of Two Arrays

def findThePrefixCommonArray(A,B):
    n=len(A)
    c=[]
    seen=set()
    count=0
    for i in range(n):
        if A[i] in seen:
            count+=1
        else:
            seen.add(A[i])
        
        if B[i] in seen:
            count+=1
        else:
            seen.add(B[i])

        c.append(count)

    return c
A = [1,2,3,4,5,6,7,8,9,0]
B = [0,9,8,7,6,5,4,3,2,1]
print(findThePrefixCommonArray(A,B))