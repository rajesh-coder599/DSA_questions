# 124. Binary Tree Maximum Path Sum


def maxPathSum(root):
    if not root:
        return 0
    ans=-float("inf")
    def dfs(node):
        if not node:
            return 0
        nonlocal ans
        left=max(0,dfs(node.left))
        right=max(0,dfs(node.right))
        ans=max(ans,left+node.val+right)

        return node.val+max(left,right)
    dfs(root)
    return ans