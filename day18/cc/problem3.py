# Plusle and Minun on Array


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    even=0
    odd=0
    even_min=float("inf")
    odd_max=-float("inf")
    for i in range(n):
        if i%2==0:
            even+=abs(arr[i])
            even_min=min(even_min,abs(arr[i]))
        else:
            odd+=abs(arr[i])
            odd_max=max(odd_max,abs(arr[i]))
    if even_min<odd_max:
        odd-=odd_max
        odd+=even_min
        even-=even_min
        even+=odd_max
    print(even-odd)