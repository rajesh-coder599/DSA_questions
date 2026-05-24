# 1340. Jump Game V


def maxJumps(arr,d):
    n=len(arr)
    jumps=[-1]*n

    def dfs(ind):
        ans=1
        if jumps[ind]!=-1:
            return jumps[ind]
        for i in range(ind-1,max(-1,ind-d-1),-1):
            if arr[ind]<=arr[i]:
                break
            ans=max(ans,1+dfs(i))
        
        for i in range(ind+1,min(n,ind+d+1)):
            if arr[ind]<=arr[i]:
                break

            ans=max(ans,1+dfs(i))

        jumps[ind]=ans
        return ans
    
    return max(dfs(i) for i in range(n))

arr = [6,4,14,6,8,13,9,7,10,6,12]
d=2
print(maxJumps(arr,d))
    
