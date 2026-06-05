# 965. Univalued Binary Tree


def isUnivalTree(root):
    a=set()
    def dfs(node):
        if not node:
            return
        a.add(node)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    if len(a)>1:
        return False
    return True