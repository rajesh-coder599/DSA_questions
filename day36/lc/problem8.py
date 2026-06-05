# 653. Two Sum IV - Input is a BST


def findTarget(root,k):
    a=set()
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        a.add(node.val)
        dfs(node.right)
    dfs(root)
    for i in a:
        x=k-i
        if x in a:
            return True
    return False