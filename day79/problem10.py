# 303. Range Sum Query - Immutable



class NumArray:

    def __init__(self,nums):
        self.nums=nums
        self.n=len(nums)
        self.tree=[0]*self.n
        def build(start,end,node):
            if start==end:
                self.tree[node]=self.nums[start]
                return
            mid=(start+end)//2
            build(start,mid,node*2+1)
            build(mid+1,end,node*2+2)
            self.tree[node]=self.tree[node*2+1]+self.tree[node*2+2]
        build(0,self.n-1,0)

    def sumRange(self,left,right):
        n=len(self.nums)
        def summ(start,end,l,r,node):
            if l>end or r<start:
                return 0
            if start>=l and end<=r:
                return self.tree[node]
            mid=(start+end)//2
            a=summ(start,mid,l,r,node*2+1)
            b=summ(mid+1,end,l,r,node*2+2)
            return a+b
        return summ(0,n-1,left,right,0)