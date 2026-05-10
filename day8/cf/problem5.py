# 2227E. it all went sideways

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    sufix_min=[0]*n
    sufix_min[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        sufix_min[i]=min(sufix_min[i+1],arr[i])
    
    for i in range(n-1,-1,-1):
        if arr[i]>sufix_min[i] :
            ans+=(arr[i]-sufix_min[i])
    
    extra_cube=0
    curr_cube=0
    for i in range(n-1):
        if sufix_min[i]==sufix_min[i+1] :
            curr_cube+=1
            extra_cube=max(extra_cube,curr_cube)
        else:
            curr_cube=0
    ans+=extra_cube
    print(ans)