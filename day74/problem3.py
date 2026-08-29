# 2904. Shortest and Lexicographically Smallest Beautiful String



def shortestBeautifulSubstring(s,k):
    arr=[]
    n=len(s)
    for i in range(n):
        currcount=0
        currstr=""
        for j in range(i,n):
            if s[j]=="1":
                currcount+=1
            if currcount>k:
                break
            currstr+=s[j]
            if currcount==k:
                arr.append(int(currstr))
    arr.sort()
    return arr[0]