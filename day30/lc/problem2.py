# 1945. Sum of Digits of String After Convert


def getLucky(s,k):
    dig=""
    for i in s:
        temp=ord(i)-96
        dig+=str(temp)
    dig=int(dig)
    for _ in range(k):
        a=str(dig)
        t=0
        for x in a:
            t+=int(x)
        dig=t
    return dig