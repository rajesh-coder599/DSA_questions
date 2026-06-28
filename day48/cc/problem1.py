# Exactly N plus 1 Values


t=int(input())
for _ in range(t):
    n=int(input())
    arr=[1,1]
    for i in range(1,n):
        arr.append(i**2)
    print(*arr)