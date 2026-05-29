# 129. Sum Root to Leaf Numbers



def sumNumbers(root):
    if not root:
        return 0
    ans=0
    def dfs(node,curr):
        if not node:
            return
        nonlocal ans
        curr=curr*10 + node.val
        if not node.left and not node.right:
            ans+=curr
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ans