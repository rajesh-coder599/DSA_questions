# 437. Path Sum III


def pathSum(root,targetSum):
    if not root:
        return 0
    def dfs1(node,currsum):
        if not node:
            return 0
        currsum+=node.val
        count=0
        if currsum==targetSum:
            count+=1
        count+=dfs1(node.left,currsum)
        count+=dfs1(node.right,currsum)

        return count
    def dfs2(n):
        if not n:
            return 0
        
        x=(dfs1(n,0)+dfs2(n.left)+dfs2(n.right))
        return x
    
    return dfs2(root)