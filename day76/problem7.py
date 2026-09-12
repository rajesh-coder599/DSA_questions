# 765. Couples Holding Hands



def minSwapsCouples(row):
    n=len(row)//2
    ans=0
    for i in range(0,n,2):
        a=row[i]
        b=row[i]+(1 if row[i]%2==0 else -1)
        if row[i+1] != b:
            j=row.index(b,i+1)
            row[i+1],row[j]=row[j],row[i+1]
            ans+=1
    return ans


## DSU approach
def minSwapsCouples(row):
    n=len(row)
    parent=list(range(n))
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(a,b):
        a=find(a)
        b=find(b)
        if a!=b:
            parent[b]=a
            return 1
        return 0
    ans=0
    for i in range(0,n*2,2):
        x=row[i]//2
        y=row[i+1]//2
        ans+=union(x,y)
    return ans