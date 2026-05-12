# 2192B. Flipping Binary String

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ones=s.count("1")
    zeros=s.count("0")
    if ones==0:
        print(0)
        continue
    if zeros%2==0 and ones%2 != 0 :
        print(-1)
        continue
    x="0"
    if ones<=zeros:
        if ones%2==0:
            x="1"
    if zeros%2==0:
        x="1"
    
    ans_arr=[]
    for i in range(n):
        if s[i]==x:
            ans_arr.append(i+1)
    print(len(ans_arr))
    print(*ans_arr)