# 114. Flatten Binary Tree to Linked List


def flatten(root):
    if not root:
        return None
    prev=None
    def dfs(node):
        if not node:
            return
        
        dfs(node.right)
        dfs(node.left)

        node.right=prev
        node.left=None

        prev=node

    dfs(root)
