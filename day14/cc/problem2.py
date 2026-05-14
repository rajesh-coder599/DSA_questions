# Divisible by i

t= int(input())
for _ in range(t):
    n=int(input())
    ans_arr=[0]*n
    i=n-1
    l=1
    r=n
    while l<=r and  i>=0 :
        ans_arr[i]=r
        r-=1
        i-=1
        if i>=0:
            ans_arr[i]=l
            l+=1
            i-=1
    print(*ans_arr)