# 655. Print Binary Tree


from collections import deque
def printTree(root):
    q=deque([root])
    height=0
    while q:
        height+=1
        l=len(q)
        for _ in range(l):
            a=q.popleft()
            if a.left:
                q.append(a.left)
            if a.right:
                q.append(a.right)
    ans=[["" for _ in range(2**height-1)] for _ in range(height)]
    n=2**height+1
    m=height
    x=deque([(root,0,n//2)])
    ans[0][n//2]=str(root.val)
    while q:
        l=len(x)
        for _ in range(l):
            node,r,c=x.popleft()
            if node.left:
                q.append(node.left,r+1,c-2**(height-r-2))
                ans[r+1][c-2**(height-r-2)]=str(node.left.val)
            if node.right:
                q.append(node.right,r+1,c+2**(height-r-2))
                ans[r+1][c+2**(height-r-2)]=str(node.right.val)
    return ans  