# https://codeforces.com/contest/2248/problem/A
# A. You Delete, I Delete



t=int(input())
for _ in range(t):
    s=input()
    ans=""
    one=False
    zero=False
    for i in s:
        if i=="1" and not one:
            one=True
            continue
        if i=="0" and not zero:
            zero=True
            continue
        ans+=i
    print(ans)