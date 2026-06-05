# 993. Cousins in Binary Tree

from collections import deque
def isCousins(root,x,y):
    xp=None
    yp=None
    def checkparent(node,prev):
        if not node:
            return
        nonlocal xp,yp
        if node==x :
            xp=prev
        if node==y:
            yp=prev
        checkparent(node.left,node)
        checkparent(node.right,node)
    checkparent(root,-1)
    if xp==yp:
        return False
    xdepth=0
    ydepth=0
    xq=deque([xp])
    yq=deque([yp])

    while xq:
        l=len(xq)
        for _ in range(l):
            a=xq.popleft()
            if a.left:
                xq.append(a.left)
            if a.right:
                xq.append(a.right)
        xdepth+=1
    
    while yq:
        s=len(xq)
        for _ in range(s):
            b=yq.popleft()
            if b.left:
                yq.append(b.left)
            if b.right:
                yq.append(b.right)
        ydepth+=1
    if xdepth==ydepth:
        return True
    return False

## with hash table
def isCousins(root,x,y):
    if x==y:
        return False
    if root.val==x or root.val==y:
        return False
    nodelevel={}
    q=deque([root])
    nodelevel[root]=(None,0)
    currdepth=0
    while q:
        n=len(q)
        for _ in range(n):
            temp=q.popleft()
            if temp.left:
                q.append(temp.left)
                nodelevel[temp.left.val]=(temp,currdepth+1)
            if temp.right:
                q.append(temp.right)
                nodelevel[temp.right.val]=(temp,currdepth+1)
        currdepth+=1
    a=nodelevel[x]
    b=nodelevel[y]
    if a[0]==b[0] or a[1]!=b[1]:
        return False
    return True