#  590. N-ary Tree Postorder Traversal


def postorder(root):
    if not root:
        return []
    ans=[]
    def dfs(n):
        if n==None:
            return
        for i in n.children:
            dfs(i)
        ans.append(i.val)
    dfs(root)
    return ans