# 530. Minimum Absolute Difference in BST


def getMinimumDifference(root):
    arr=[]
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        arr.append(node.val)
        dfs(node.right)
    dfs(root)
    ans=float("inf")
    for i in range(len(arr)-1):
        ans=min(ans,abs(arr[i]-arr[i+1]))
    return ans