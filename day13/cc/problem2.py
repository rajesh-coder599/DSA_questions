# Chef and Glove

t=int(input())
for _ in range(t):
    n=int(input())
    finger=list(map(int,input().split()))
    glove=list(map(int,input().split()))
    front=True
    back=True
    for i in range(n):
        temp=glove[i]
        if finger[i]>temp:
            front=False
        if finger[n-i-1]>temp:
            back=False
    if front and back:
        print("both")
    elif front:
        print("front")
    elif back:
        print("back")
    else:
        print("none")