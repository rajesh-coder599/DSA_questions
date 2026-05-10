# 1030A. in search of an easy problem
n=int(input())
opinion=list(map(int,input().split()))
ans="easy"
for i in opinion:
    if i==1:
        ans="hard"
        break

print(ans)