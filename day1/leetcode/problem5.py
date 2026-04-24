# 2900. Longest Unequal Adjacent Groups Subsequence I

words = ["a","b","c","d"]
groups = [1,0,1,1]

n=len(words)
ans=[]
ans.append(words[0])
for i in range(1,n):
    if groups[i]==groups[i-1] :
        continue
    ans.append(words[i])

print(ans)