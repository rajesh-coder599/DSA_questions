# Q1. Exactly One Consecutive Set Bits Pair©leetcode

def consecutiveSetBits(n):
    b=bin(n)[2:]
    pair=0
    for i in range(len(b)-1):
        if b[i]=="1" and b[i+1]=="1":
            pair+=1
    return pair==1