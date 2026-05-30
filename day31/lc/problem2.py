# 1376. Time Needed to Inform All Employees

from collections import deque
def numOfMinutes(n,headID,manager,informTime):
    q=deque()
    q.append(headID)
    ans=0
    while q:
        l=len(q)
        for _ in range(q):
            a=q.pop()