# 671. Second Minimum Node In a Binary Tree



def findSecondMinimumValue(root):
    a=set()
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        a.add(node.val)
        dfs(node.right)
    dfs(root)
    a.remove(min(a))
    if len(a)==0:
        return -1
    return min(a)