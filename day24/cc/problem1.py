# Make Array Odd

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    even_count=0
    odd_count=0
    for i in a:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1

    if x%2==0:
        if odd_count>0:
            print(even_count)
        else:
            print(-1)
    else:
        if even_count%2==0:
            print(even_count//2)
        else:
            print(even_count//2+1)