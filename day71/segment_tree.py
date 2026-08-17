# today we are learning new data structure called segment tree which is used to do range queries in array


arr=[2, 1, 5, 3, 4]
n=len(arr)
tree=[0]*(4*n)
def build(node,l,r):
    if l==r:
        tree[node]=arr[l]
        return
    mid=(l+r)//2
    build(node*2,l,mid)
    build(node*2+1,mid+1,r)
    tree[node]=tree[node*2]+tree[node*2+1]
build(1,0,n-1)
print(tree)
def query(node,l,r,ql,qr):
    if qr<l or ql>r:
        return 0
    if ql<=l and r<=qr:
        return tree[node]
    mid=(l+r)//2
    left=query(node*2,l,mid,ql,qr)
    right=query(node*2+1,mid+1,r,ql,qr)
    return left+right
print(query(1,0,n-1,0,2))
def update(node,l,r,idx,val):
    if l==r:
        tree[node]=val
        return
    mid=(l+r)//2
    if idx<=mid:
        update(node*2,l,mid,idx,val)
    else:
        update(node*2+1,mid+1,r,idx,val)
    tree[node]=tree[node*2]+tree[node*2+1]
