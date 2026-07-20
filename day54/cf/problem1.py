# https://codeforces.com/problemset/problem/2242/B
# B. Predominant Frequency Division


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    one=0
    two=0
    three=0
    first=False
    second=False
    for i in range(n):
        if arr[i]==1:
            one+=1
        elif arr[i]==2:
            two+=1
        else:
            three+=1
        if not first:
            if one==two+three:
                first=True
                one,two,three=0,0,0
            elif one>two+three :
                if i<n-1 and arr[i+1]==3:
                    continue
                else:
                    first=True
                    one,two,three=0,0,0
        else:
            if one+two>=three and i<n-1:
                second=True
                break
    if first and second :
        print("YES")
    else:
        print("NO")