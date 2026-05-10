# 2145B. Deck of cards

t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    ans=["+"]*n
    for i in range(k):
        if s[i]=="0":
            ans[i]="-"
        elif s[i]=="1" :
            ans[n-i-1]="-"
        else:
            ans[i]="?"
            ans[n-i-1]="?"

    final_ans="".join(ans)
    print(final_ans)