# 515. Find Largest Value in Each Tree Row

from collections import deque
def largestValues(root):
    if not root:
        return []
    ans=[root.val]
    q=deque([root])
    while q:
        l=len(q)
        mx=float("inf")
        for _ in range(l):
            a=q.popleft()
            if a.left:
                q.append(a.left)
                mx=max(mx,a.left.val)
            if a.right:
                q.append(a.right)
                mx=max(mx,a.right.val)
        if mx!=float("inf"):
            ans.append(mx)
    return ans