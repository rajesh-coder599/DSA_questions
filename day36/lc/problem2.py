# 404. Sum of Left Leaves

from collections import deque
def sumOfLeftLeaves(root):
    if not root.left and not root.right:
        return 0
    
    def dfs(node,parent):
        if not node.left and not node.right:
            if parent.left==node:
                return node.val
            return 0
        
        leftsum=dfs(node.left,node)+dfs(node.right,node)
        return leftsum
    return dfs(root,-1)

## BFS
def sumOfLeftLeaves(root):
    if not root.left and not root.right:
        return 0
    q=deque([root])
    ans=0
    while q:
        a=q.popleft()
        if a.left:
            q.append(a.left)
            x=a.left
            if not x.left and not x.right:
                ans+=x.val
        if a.right:
            q.append(a.right)
    return ans