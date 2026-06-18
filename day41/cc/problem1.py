# Anti Palindrome

from collections import defaultdict
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    freq=defaultdict(int)
    for i in s:
        freq[i]+=1
    oddcount=0
    evencount=0
    for v in freq.values():
        if v%2==0:
            evencount+=1
        else:
            oddcount+=1
    if n%2==0:
        if oddcount != 0:
            print(0)
        else:
            print(1)
    else:
        if oddcount != 1:
            print(0)
        else:
            print(1 if evencount>0 else 2)