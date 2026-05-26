# 226. Invert Binary Tree

def invertTree(root):
    if root==None:
        return None
    root.left,root.right=root.right,root.left
    invertTree(root.left)
    invertTree(root.right)

    return root