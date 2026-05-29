# 116. Populating Next Right Pointers in Each Node

from collections import deque
def connect(root):
    if not root:
        return
    q=deque()
    q.append(root)
    while q:
        l=len(q)
        prev=None
        for _ in range(l):
            a=q.popleft()
            if prev:
                prev.next=a
            prev=a
            if a.left:
                q.append(a.left)
            if a.right :
                q.append(a.right)
    return root

## with dfs :
def connect(root):
    if not root:
        return
    def dfs(node):
        if not node:
            return
        
        node.left.next=node.right
        if node.next:
            node.right.next=node.next.left
        
        dfs(node.left)
        dfs(node.right)
        return node
    return dfs(root)