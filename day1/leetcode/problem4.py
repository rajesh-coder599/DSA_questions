# 1668. Maximum Repeating Substring


sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"
x=sequence.count(word)
print(x)
# m=len(word)
# max_rep=0
# c=0
# rep=0
# for i in sequence :
#     if i==word[c]:
#         c+=1
#     elif i==word[0]:
#         c=1
#     else:
#         c=0
#     if c==m:
#         max_rep+=1
#         c=0
# print(max_rep)