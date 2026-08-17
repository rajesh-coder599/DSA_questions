# 307. Range Sum Query - Mutable



class NumArray:

    def __init__(self,nums):
        self.nums=nums
        self.n=len(nums)
        self.tree=[0]*(4*self.n)
        self.build(1,0,self.n-1)
    def build(self,node,l,r):
        if l==r:
            self.tree[node]=self.nums[l]
            return
        mid=(l+r)//2
        self.build(node*2,l,mid)
        self.build(node*2+1,mid+1,r)
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1]
    def update_tree(self,node,l,r,idx,val):
        if l==r:
            self.tree[node]=val
            return
        mid=(l+r)//2
        if mid<=idx:
            self.update_tree(node*2+1,mid+1,r,idx,val)
        else:
            self.update_tree(node*2,l,mid,idx,val)
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1]
    def update(self,index,val):
        self.update_tree(1,0,self.n-1,index,val)
    def query(self,node,l,r,ql,qr):
        if ql>r or qr<l:
            return 0
        if ql<=l and r<=qr:
            return self.tree[node]
        mid=(l+r)//2
        left=self.query(node*2,l,mid,ql,qr)
        right=self,self.query(node*2+1,mid+1,ql,qr)
        return left+right
    def sumRange(self,left,right):
        return self.query(1,0,self.n-1,left,right)