# 1871. Jump Game VII


def canReach(s, minJump, maxJump):
    if s[-1]==1:
        return False
    n=len(s)
    dp=[False]*n
    def dfs(ind):
        if ind==n-1:
            return True
        
        dp[ind]=True
        for i in range(ind+minJump,min(n-1,ind+maxJump)+1):
            if s[i]=="0" and dp[i]==False:
                if dfs(i):
                    return True
                
        return False
    return dfs(0)

s = "011010"
mn=2
mx=3
print(canReach(s,mn,mx))

from collections import deque
## better approach
def cr(s, minJump, maxJump):
    if s[-1]=="1":
        return False
    n=len(s)

    q=deque([0])
    far=0
    while q:

        ind=q.popleft()
        start=max(ind+minJump,far+minJump)
        end=min(n-1,ind+maxJump)
        for i in range(start,end+1):
            if s[i]=="0":
                if i==n-1:
                    return True
                q.append(i)
        far=end
    return False
print(cr(s,mn,mx))