# Reversing directions

t=int(input())
for _ in range(t):
    n=int(input())
    directions=[input() for _ in range(n)]
    prev=None
    for i in range(n-1,-1,-1):
        a=directions[i].split()
        if prev==None:
            prev=a[0]
            a[0]="Begin"
        elif prev=="Right" :
            prev=a[0]
            a[0]="Left"
        else:
            prev=a[0]
            a[0]="Right"

        ans=" ".join(a)
        print(ans)