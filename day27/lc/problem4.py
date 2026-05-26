# 429. N-ary Tree Level Order Traversal

from collections import deque
def levelOrder(root):
    if root==None:
        return None
    ans=[[root.val]]
    q=deque([root])
    while q:
        l=len(q)
        temp=[]
        for _ in range(l):
            a=q.popleft()
            if a.children!=None:
                for i in a.children:
                    temp.append(i.val)
                    q.append(i)
        
        if len(temp)>0:
            ans.append(temp)
    return ans