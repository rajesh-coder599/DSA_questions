# 1668. Maximum Repeating Substring


sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"

k=0
while word*(k+1) in sequence :
    k+=1
print(k)