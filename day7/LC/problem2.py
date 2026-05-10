# 3713 llongest balanced substring

s="abbac"
n=len(s)
freq={}

for i in range(n):
    ch=s[i]
    if ch not in freq:
        freq[ch]=[0]*n

    for j in range(i,n):
        freq[ch][j]+=1

ans=1
for i in range(n):
    for j in range(i,n):
        check=-1
        temp=True
        for k,v in freq.items():
            curr=v[j]-(v[i-1] if i>0 else 0)
            if curr==0:
                continue
            if check == -1 :
                check=curr

            

            if check != curr :
                temp=False
                break
        
        if temp:
            ans=max(ans,j-i+1)

print(ans)