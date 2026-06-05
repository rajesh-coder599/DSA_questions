# 617. Merge Two Binary Trees


from collections import deque
def mergeTrees(root1,root2):
    def dfs(node1,node2):
        if not node1:
            return node2
        if not node2:
            return node1
        
        node1.val+=node2.val
        node1.left=dfs(node1.left,node2.left)
        node1.right=dfs(node1.right,node2.right)
        return node1
    
    return dfs(root1,root2)

def mergeTrees(root1,root2):
    if not root1:
        return root2
    if not root2:
        return root1
    q=deque([(root1,root2)])
    while q:

        node1,node2=q.popleft()
        node1.val+=node2.val
        if node1.left and node2.left:
            q.append((node1.left,node2.left))
        elif not node1.left:
            node1.left=node2.left
        if node1.right and node2.right:
            q.append((node1.right,node2.right))
        elif not node1.right:
            node1.right=node2.right  
    return root1