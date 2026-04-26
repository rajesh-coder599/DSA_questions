# contest 2222 : A Wonderful Contest

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if 100 in arr :
        print("YES")
    else:
        print("NO")