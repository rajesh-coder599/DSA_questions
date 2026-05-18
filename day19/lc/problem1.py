# 1345. Jump Game IV
from collections import defaultdict , deque
arr = [7,6,9,6,9,6,9,7]
def minJumps(arr):
    n=len(arr)
    if n==1:
        return 0
    graph=defaultdict(list)
    for i,val in enumerate(arr):
        graph[val].append(i)

    q=deque([0])
    visited=[False]*n
    steps=0
    visited[0]=True

    while len(q) !=0 :
        temp=len(q)
        for _ in range(temp):

            a=q.popleft()
            if a==n-1:
                return steps
            if a-1>=0 and not visited[a-1]:
                q.append(a-1)
                visited[a-1]=True

            if a+1<=n-1 and not visited[a+1]:
                q.append(a+1)
                visited[a+1]=True

            if arr[a] in graph:
                for i in graph[arr[a]]:
                    if not visited[i] :
                        visited[i]=True
                        q.append(i)
                del graph[arr[a]]
        steps+=1
    return steps

print(minJumps(arr))