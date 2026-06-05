# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree


def getTargetCopy(original,cloned,target):
    def dfs(node1,node2):
        if not node1 or not node2:
            return
        if target==node1:
            return node2
        return dfs(node1.left,node2.left) or dfs(node1.right,node2.right)
    return dfs(original,cloned)