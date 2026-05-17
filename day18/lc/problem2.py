# 1306. Jump Game III

arr = [3,0,2,1,2]
start = 2

def rec(i,arr,vis):
    n=len(arr)
    if i<0 or i>=n:
        return False
    if arr[i]==0:
        return True
    if i in vis :
        return False
    vis.add(i)
    
    return rec(i-arr[i],arr,vis) or rec(i+arr[i],arr,vis)

print(rec(start,arr,set()))