# 2641. Cousins in Binary Tree II

from collections import deque
def replaceValueInTree(root):
    levelsum={0:root.val}
    q=deque([root])
    currdepth=0
    while q:
        currdepth+=1
        l=len(q)
        currsum=0
        for _ in range(l):
            a=q.popleft()
            if a.left:
                currsum+=a.left.val
                q.append(a.left)
            if a.right:
                currsum+=a.right.val
                q.append(a.right)
        levelsum[currdepth]=currsum
    x=deque([root])
    root.val=0
    d=0
    while x:
        d+=1
        l=len(x)
        for _ in range(l):
            temp=0
            node=x.popleft()
            if node.left:
                temp+=node.left.val
                x.append(node.left)
            if node.right:
                temp+=node.right.val
                x.append(node.right)
            if node.left:
                node.left.val=levelsum[d]-temp
            if node.right:
                node.right.val=levelsum[d]-temp
    return root