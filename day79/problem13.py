# 2569. Handling Sum Queries After Update

def handleQuery(nums1,nums2,queries):
    n=len(nums1)
    tree=[(0,0)]*(4*n)
    lazy=[1]*(4*n)
    def build(start,end,node):
        if start==end:
            if nums1[start]==1:
                tree[node]=(1,0)
            else:
                tree[node]=(0,1)
            return
        mid=(start+end)//2
        build(start,mid,node*2+1)
        build(mid+1,end,node*2+2)
        tree[node]=(tree[node*2+1][0]+tree[node*2+2][0],tree[node*2+1][1]+tree[node*2+2][1])
    build(0,n-1,0)
    def push(start,end,node):
        if lazy[node]==1:
            return
        if start==end:
            lazy[node]=1
            return
        left=node*2+1
        right=node*2+2
        tree[left]=(tree[left][1],tree[left][0])
        tree[right]=(tree[right][1],tree[right][0])
        lazy[left]*=-1
        lazy[right]*=-1
        lazy[node]=1
    def flip(start,end,node,l,r):
        if l>end or r<start:
            return 
        if l<=start and end<=r:
            tree[node]=(tree[node][1],tree[node][0])
            if start!=end:
                lazy[node]*=-1
            return
        push(start,end,node)
        mid=(start+end)//2
        flip(start,mid,node*2+1,l,r)
        flip(mid+1,end,node*2+2,l,r)
        tree[node]=(tree[node*2+1][0]+tree[node*2+2][0],tree[node*2+1][1]+tree[node*2+2][1])
    val=sum(nums2)
    result=[]
    for q,x,y in queries:
        if q==1:
            flip(0,n-1,0,x,y)
        elif q==2:
            val+=tree[0][0]*x
        else:
            result.append(val)
    return result