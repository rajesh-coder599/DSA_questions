# 559. Maximum Depth of N-ary Tree

from collections import deque
def maxDepth(root):
    if not root:
        return 0
    ans=0
    q=deque([root])
    while q:
        l=len(q)
        check=False
        for _ in range(l):
            a=q.popleft()
            if a.children :
                q+=a.children
                check=True
        ans+=1
    return ans

#DFS
def maxDepth(root):
    if not root:
        return 0
    def dfs(node,level):
        if not node:
            return
        for i in node.children:
            dfs(node,level+1)
        
        return level
    return dfs(root,0)