# https://codeforces.com/contest/2252/problem/B
# B. Always Changing



t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ones=s.count("1")
    zeros=s.count("0")
    if abs(ones-zeros)>2:
        print(-1)
        continue
    sameadj=[0,0]
    for i in range(n-1):
        if s[i]==s[i+1]:
            if s[i]=="1":
                sameadj[1]+=1
            else:
                sameadj[0]+=1
    if sameadj[0]==sameadj[1]:
        print(sum(sameadj))
    else:
        print(max(sameadj)*2-1)
        