# Weird Palindrome Making


t=int(input())
for _ in range(t):
    n=int(input())
    al=list(map(int,input().split()))
    odd_count=0
    total=0
    for i in al:
        if i%2==1:
            odd_count+=1
        total+=i
    if total%2==1:
        odd_count-=1
    ans=odd_count//2+(1 if odd_count%2==1 else 0)
    print(ans)