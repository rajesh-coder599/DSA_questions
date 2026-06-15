# 2196. Create Binary Tree From Descriptions


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(descriptions):
    nodes={}
    parent=set()
    notparent=set()
    for i,j,k in descriptions:
        x=TreeNode(i)
        y=TreeNode(j)
        if i not in nodes:
            nodes[i]=x
            parent
        if j not in nodes:
            nodes[j]=y
        parent.add(i)
        notparent.add(j)
    root=None
    for i in parent:
        if i not in notparent:
            root=nodes[i]
            break
    for a,b,c in descriptions:
        if c==1:
            nodes[a].left=nodes[b]
        else:
            nodes[a].right=nodes[b]
    return root