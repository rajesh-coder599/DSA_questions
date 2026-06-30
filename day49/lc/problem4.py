# 990. Satisfiability of Equality Equations



def equationsPossible(equations):
    parent=list(range(26))
    def find(x):
        if parent[x] != x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(a,b):
        pa=find(a)
        pb=find(b)
        if pa!=pb:
            parent[pa]=pb
    for eq in equations:
        if eq[1]=="=":
            a=ord(eq[0])-97
            b=ord(eq[3])-97
            union(a,b)
    for eq in equations:
        if eq[1]=="!":
            a=ord(eq[0])-97
            b=ord(eq[3])-97
            if find(a)==find(b):
                return False
    return True