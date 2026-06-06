# 623. Add One Row to Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
def addOneRow(root,val,depth):
    newnode=TreeNode(val)
    if depth==1:
        newnode.left=root
        return newnode
    d=0
    q=deque([root])
    while q:
        d+=1
        l=len(q)
        check=False
        for _ in range(l):
            a=q.popleft()
            if d==depth-1:
                check=True
                if a.left:
                    temp=TreeNode(val)
                    temp.left=a.left
                    a.left=temp
                else:
                    a.left=TreeNode(val)
                if a.right:
                    x=TreeNode(val)
                    x.right=a.right
                    a.right=x
                else:
                    a.right=TreeNode(val)
            else:
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
        if check:
            return root