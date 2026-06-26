# 721. Accounts Merge



def accountsMerge(accounts):
    numofname={}
    n=len(accounts)
    for i in range(n):
        numofname[i]=accounts[i][0]
    parent=list(range(n))
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    ac={}
    for i in range(n):
        for j in accounts[i][1:]:
            if j in ac:
                root1=find(ac[j])
                root2=find(i)
                if root1 != root2 :
                    parent[root1]=root2
            else:
                ac[j]=i
    conect={}
    for i in range(n):
        root=find(i)
        if root in conect:
            conect[root]+=accounts[i][1:]
        else:
            conect[root]=accounts[i][1:]
    ans=[]
    for k,v in conect.items():
        temp=[numofname[k]]
        b=list(set(v))
        b.sort()
        temp+=b
        ans.append(temp)
    return ans
accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
print(accountsMerge(accounts))