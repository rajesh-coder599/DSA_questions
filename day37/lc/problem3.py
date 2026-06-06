# 449. Serialize and Deserialize BST



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:

    def serialize(root):
        s="-1"
        def preorder(node):
            if not node:
                return
            nonlocal s
            s+=("#"+str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return s
    def deserialize(data):
        arr=list(map(int,data.split("#")))[1:]
        i=0
        def build(low,high):
            nonlocal i
            if i==len(arr):
                return
            if arr[i]<low or arr[i]>high:
                return
            root=TreeNode(arr[i])
            i+=1
            root.left=build(low,root.val)
            root.right=build(root.val,high)
            return root

        return build(-float("inf"),float("inf"))