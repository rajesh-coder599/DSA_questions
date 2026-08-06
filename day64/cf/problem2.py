# https://codeforces.com/problemset/problem/2245/B
# B. Delete and Concatenate



t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    arr=list(map(int,input().split()))
    smaller_count=0
    score=0
    smaller=[]
    for i in arr:
        if i<c:
            smaller_count+=1
            smaller.append(i)
        else:
            score+=(i-c)
    graterorequal_count=n-smaller_count
    if graterorequal_count<smaller_count:
        smaller.sort(reverse=True)
        x=smaller_count-graterorequal_count
        for i in range(x//2+x%2):
            score+=(smaller[i]-c)
    print(score)