# 2265. Count Nodes Equal to Average of Subtree



def averageOfSubtree(root):
    if not root:
        return 0
    ans=0
    def solve(node):
        nonlocal ans
        if not node:
            return 0,0
        leftsum,leftcount=solve(node.left)
        rightsum,rightcount=solve(node.right)
        total_count=1+leftcount+rightcount
        total_sum=node.val+leftsum+rightsum
        if total_sum//total_count==node.val:
            ans+=1
        return total_sum,total_count
    solve(root)
    return ans