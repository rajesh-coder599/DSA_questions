# https://codeforces.com/contest/2254/problem/B
# B. Evanescent


t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ans=1
    prevlen=1
    track=0
    for i in range(1,n):
        if s[i] != s[i-1] :
            ans+=1
            if prevlen==1 and i>=2:
                if s[i-2]!=s[i]:
                    track=max(1,track)
                else:
                    track=2
            prevlen=1
        else:
            prevlen+=1
    ans-=track
    print(ans)