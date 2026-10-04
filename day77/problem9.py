# 1080. Insufficient Nodes in Root to Leaf Paths




def sufficientSubset(root,limit):
    def solve(node,l):
        if not node:
            return
        l-=node.val
        if not node.left and not node.right:
            if l>0:
                return
            return node
        node.left=solve(node.left,l)
        node.right=solve(node.right,l)
        if not node.left and not node.right:
            return
        return node
    return solve(root,limit)