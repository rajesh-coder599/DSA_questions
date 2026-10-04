# 3498. Reverse Degree of a String



# def reverseDegree(s):
#     ans=0
#     n=len(s)
#     for i in range(n):
#         x=s[i]
#         temp=(123-ord(x))*(i+1)
#         ans+=temp
#     return ans

###
n=20
star="*"
for i in range(n):
    space=" "*(n-i-1)
    temp=space+star+space
    print(temp)
    star+=" *"