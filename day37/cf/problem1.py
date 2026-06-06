# A. Pangram


n=int(input())
s=input()
a=set(s.lower())
x="abcdefghijklmnopqrstuvwxyz"
check=True
for i in x:
    if i not in a:
        check=False
        break
if check:
    print("YES")
else:
    print("NO")