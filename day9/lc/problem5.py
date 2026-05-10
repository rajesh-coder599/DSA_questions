# 3714 longest substring part2


def  findkey(key,s):
    freq={"a":0,"b":0,"c":0}
    for i in s:
        freq[i]+=1
    if [freq["a"]-freq["b"],freq["b"]-freq["c"]]==key :
        return True
    return False
s="aabcc"
n=len(s)
freq={"a":[0]*n,
      "b":[0]*n,
      "c":[0]*n}

freq[s[0]][0]=1
for i in range(1,n):
    if s[i]=="a":
        freq["a"][i]=1+freq["a"][i-1]
    else:
        freq["a"][i]=freq["a"][i-1]

for i in range(1,n):
    if s[i]=="b":
        freq["b"][i]=1+freq["b"][i-1]
    else:
        freq["b"][i]=freq["b"][i-1]

for i in range(1,n):
    if s[i]=="c":
        freq["c"][i]=1+freq["c"][i-1]
    else:
        freq["c"][i]=freq["c"][i-1]

key=[freq["a"][-1]-freq["b"][-1],freq["b"][-1]-freq["c"][-1]]
ind=None
for i in range(n):
    if findkey(key,s[:i]):
        ind=i
        break

if ind != None :
    print(s[i+1:])
else:
    print(0)