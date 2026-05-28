# 543. Diameter of Binary Tree


def diameterOfBinaryTree(root):
        if not root:
            return 0
        ans=0
        def dfs(node):
            nonlocal ans

            if not node:
                return 0
            
            left=dfs(node.left)
            right=dfs(node.right)

            ans=max(ans,left+right)
        
        dfs(root)
        return ans