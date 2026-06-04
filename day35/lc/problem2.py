# 230. Kth Smallest Element in a BST


def kthSmallest(root,k):
    if not root.left and not root.right:
        return root.val
    n=k
    value=root.val
    def dfs(node):
        if not node:
            return
        nonlocal n,value
        if n==0 :
            return
        dfs(node.left)
        n-=1
        if n==0:
            value=node.val

        dfs(node.right)
    
    return dfs(root)