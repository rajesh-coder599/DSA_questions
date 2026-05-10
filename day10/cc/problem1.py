# break the stick

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    if x%2 != 0 :
        print(True)
    elif (n-x)%2 == 0 :
        print(True)
    else:
        print(False)


