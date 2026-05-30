# 2232C1. Seating Arrangement (Easy Version)


t=int(input())
for _ in range(t):
    n,x,s=map(int,input().split())
    friends=input()
    tables=[s]*x
    ans=0
    for k in range(n):
        i=friends[i]
        if i=="I" :
            for a in range(x):
                if tables[a]==s:
                    ans+=1
                    tables[a]-=1
                    break
        elif i=="E" :
            for b in range(x):
                if 0<tables[b]<s:
                    ans+=1
                    tables[b]-=1
                    break
        else:
            ec=0
            ic=tables.count(s)
            for c in range(x):
                if 0<tables[c]<s:
                    ec+=tables[c]
            if ic==0 or ec==0 or ic==x:
                for l in range(x):
                    if tables[l]==s:
                        ans+=1
                        tables[l]-=1
                        break
                continue
            fe=0
