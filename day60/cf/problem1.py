# https://codeforces.com/problemset/problem/344/A
# A. Magnets


n=int(input())
ans=0
prev=None
for _ in range(n):
    pole=input()
    if prev==None:
        prev=pole[1]
        ans+=1
    elif prev==pole[0]:
        ans+=1
        prev=pole[1]
print(ans)