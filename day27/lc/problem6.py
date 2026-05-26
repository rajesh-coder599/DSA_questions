# 589. N-ary Tree Preorder Traversal


def preorder(root):
    ans=[]
    def dfs(node):
        if not node:
            return
        ans.append(node.val)
        for i in node.children:
            dfs(i)
    dfs(root)
    return ans