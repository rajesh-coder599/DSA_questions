# 3187. Peaks in Array



def countOfPeaks(nums,queries):
    n=len(nums)
    tree=[0]*(4*n)
    def build(start,end,node):
        if start==end:
            if not (start==0 or start==n-1) and nums[start-1]<nums[start]>nums[start+1]:
                tree[node]=1
            return
        mid=(start+end)//2
        build(start,mid,node*2+1)
        build(mid+1,end,node*2+2)
        tree[node]=tree[node*2+1]+tree[node*2+2]
    build(0,n-1,0)
    def update(start,end,node,idx):
        if start==end:
            if start==0 or start==n-1:
                tree[node]=0
            elif nums[start-1]<nums[start]>nums[start+1]:
                tree[node]=1
            else:
                tree[node]=0
            return
        mid=(start+end)//2
        if idx<=mid:
            update(start,mid,node*2+1,idx)
        else:
            update(mid+1,end,node*2+2,idx)
        tree[node]=tree[node*2+1]+tree[node*2+2]
    def peak_ele_count(start,end,l,r,node):
        if l>end or r<start:
            return 0
        if l<=start and r>=end:
            return tree[node]
        mid=(start+end)//2
        left=peak_ele_count(start,mid,l,r,node*2+1)
        right=peak_ele_count(mid+1,end,l,r,node*2+2)
        return left+right
    result=[]
    for q in queries:
        typ=q[0]
        if typ==1:
            li=q[1]
            ri=q[2]
            if ri-li<=1:
                result.append(0)
            else:
                temp=peak_ele_count(0,n-1,li+1,ri-1,0)
                result.append(temp)
        else:
            i=q[1]
            v=q[2]
            nums[i]=v
            for idx in range(max(0,i-1),min(n-1,i+1)+1):
                update(0,n-1,0,idx)
    return result

arr=[3,1,4,2,5]
q=[[2,3,4],[1,0,4]]
print(countOfPeaks(arr,q))