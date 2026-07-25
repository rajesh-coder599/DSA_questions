# https://codeforces.com/problemset/problem/2222/B
# B. Artistic Balance Tree



t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    x=list(map(int,input().split()))
    oddposition=[]
    evenposition=[]
    oddmarked=False
    evenmarked=False
    for i in range(n):
        if i%2==0:
            evenposition.append(a[i])
        else:
            oddposition.append(a[i])
    oddposition.sort()
    evenposition.sort()
    for i in x:
        i-=1
        if i%2==0 and evenposition:
            if evenposition[-1]>=0:
                evenposition.pop()
                evenmarked=True
            else:
                if not evenmarked:
                    evenmarked=True
                    evenposition.pop()
        if i%2!=0 and oddposition :
            if oddposition[-1]>=0:
                oddposition.pop()
                oddmarked=True
            else:
                if not oddmarked:
                    oddmarked=True
                    oddposition.pop()
    print(sum(oddposition)+sum(evenposition))