# 662. Maximum Width of Binary Tree

from collections import deque
def widthOfBinaryTree(root):
    if not root.left and not root.right:
        return 1
    mxwidth=1
    q=deque([root])
    while q:
        l=len(q)
        temp=[]
        for _ in range(l):
            a=q.popleft()
            if a=="#":
                temp+=["#","#"]
            else:
                if a.left:
                    temp.append(a.left)
                else:
                    temp.append("#")
                if a.right:
                    temp.append(a.right)
                else:
                    temp.append("#")
        firstnode=None
        lastnode=None
        for i in range(len(temp)):
            if temp[i]!="#":
                firstnode=i
                break
        for j in range(len(temp)-1,-1,-1):
            if temp[j]!="#":
                lastnode=j
                break
        if firstnode is None and lastnode is None:
            continue
        x=temp[firstnode:lastnode+1]
        mxwidth=max(mxwidth,len(x))
        for k in x:
            q.append(k)
    return mxwidth

## space optimized
def widthOfBinaryTree(root):
    if not root.left and not root.right:
        return 1
    ans=1
    q=deque([(root,0)])
    while q:
        l=len(q)
        first=q[0][1]
        last=q[-1][1]
        ans=max(ans,last-first+1)
        for _ in range(l):
            node,idx=q.popleft()
            idx-=first
            if node.left:
                q.append((node.left,2*idx))
            if node.right:
                q.append((node.right,2*idx+1))
    return ans