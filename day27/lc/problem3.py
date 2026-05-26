# 2415. Reverse Odd Levels of Binary Tree

from collections import deque
def reverseOddLevels(root):
    
    level=1
    q=deque([root])

    while q:
        l=len(q)
        n=[]
        v=[]
        for _ in range(l):
            a=q.popleft()
            n.append(a)
            v.append(a.val)
            if a.left != None :
                q.append(a.left)
            if a.right != None :
                q.append(a.right)
        if level%2==1 :
            v.reverse()
            for i in range(l):
                n[i].val=v[i]
        level+=1
    return root