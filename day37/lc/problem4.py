# 513. Find Bottom Left Tree Value

from collections import deque
def findBottomLeftValue(root):
    q=deque([root])
    arr=[[root.val]]
    while q:
        l=len(q)
        temp=[]
        for _ in range(l):
            a=q.popleft()
            if a.left:
                temp.append(a.left.val)
                q.append(a.left)
            if a.right:
                temp.append(a.right.val)
                q.append(a.right)
        if len(temp)>0:
            arr.append(temp)
    for i in range(len(arr)-1,-1,-1):
        return arr[i][0]
    
def findBottomLeftValue(root):
    depth=0
    ans=root.val
    def dfs(node,d):
        if not node:
            return
        nonlocal depth,ans
        if d>depth:
            depth=d
            ans=node.val
        dfs(node.left,d+1)
        dfs(node.right,d+1)
    dfs(root,0)
    return ans