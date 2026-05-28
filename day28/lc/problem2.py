# 113. Path Sum II


def pathSum(root,targetSum):
    if root==None:
        return []
    
    ans=[]
    path=[]
    def dfs(node,currsum):
        if node==None:
            return
        currsum+=node.val
        path.append(node.val)
        if not node.left and not node.right :
            if currsum==targetSum :
                ans.append(path[:])
        dfs(node.left,currsum)
        dfs(node.right,currsum)

        path.pop()
    
    dfs(root,0)
    return ans